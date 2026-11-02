// Staff lock: Vercel Routing Middleware. Basic auth on /staff and /staff/*, against STAFF_USER (default "staff")
// and STAFF_PASSWORD. No password set: 503 "locked". Wrong password: 401. Set STAFF_PASSWORD in Vercel, never in code.
import { next } from '@vercel/functions';

export const config = { matcher: ['/staff', '/staff/:path*'] };

const enc = new TextEncoder();
function safeEqual(a, b) {
  const x = enc.encode(a), y = enc.encode(b);
  const len = Math.max(x.length, y.length);
  let diff = x.length ^ y.length;
  for (let i = 0; i < len; i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
}
const base = { 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex, nofollow', 'Content-Type': 'text/plain; charset=utf-8' };

export default function middleware(request) {
  const pass = process.env.STAFF_PASSWORD;
  const user = process.env.STAFF_USER || 'staff';
  if (!pass) return new Response('Locked: the staff password is not set yet.', { status: 503, headers: base });
  const auth = request.headers.get('authorization') || '';
  if (auth.startsWith('Basic ')) {
    let decoded = '';
    try { decoded = atob(auth.slice(6)); } catch (e) { decoded = ''; }
    const i = decoded.indexOf(':');
    if (i > -1) {
      const okUser = safeEqual(decoded.slice(0, i), user);
      const okPass = safeEqual(decoded.slice(i + 1), pass);
      if (okUser & okPass) return next();
    }
  }
  return new Response('Authentication required.', { status: 401, headers: { ...base, 'WWW-Authenticate': 'Basic realm="CODED staff", charset="UTF-8"' } });
}
