// Staff password for /staff (trainer pages and backup videos). Vercel Routing Middleware, runs before the cache.
// Set STAFF_PASSWORD (and optionally STAFF_USER, default "staff") in Vercel: Project Settings > Environment Variables.
// No password set = the staff pages stay locked.
import { next } from '@vercel/functions';

export const config = { matcher: ['/staff', '/staff/:path*'] };

function same(a, b) {
  // compare without stopping at the first different character
  if (typeof a !== 'string' || typeof b !== 'string') return false;
  let diff = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) diff |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  return diff === 0;
}

export function allowed(authHeader, user, pass) {
  if (!pass || !authHeader || !authHeader.startsWith('Basic ')) return false;
  let decoded = '';
  try { decoded = atob(authHeader.slice(6).trim()); } catch { return false; }
  const i = decoded.indexOf(':');
  if (i < 0) return false;
  return same(decoded.slice(0, i), user) && same(decoded.slice(i + 1), pass);
}

export default function middleware(request) {
  const user = process.env.STAFF_USER || 'staff';
  const pass = process.env.STAFF_PASSWORD;
  const noStore = { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex, nofollow' };
  if (!pass) return new Response('Staff pages are locked. Set STAFF_PASSWORD in the Vercel project settings.', { status: 503, headers: noStore });
  if (allowed(request.headers.get('authorization'), user, pass)) {
    return next({ headers: { 'cache-control': 'private, no-store', 'x-robots-tag': 'noindex, nofollow' } });
  }
  return new Response('CODED staff only.', { status: 401, headers: { ...noStore, 'www-authenticate': 'Basic realm="CODED staff", charset="UTF-8"' } });
}
