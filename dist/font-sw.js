// Font-only cache: HTML and scripts always follow normal network caching.
const CACHE = 'technical-writing-fonts-v1';
const FONT_PATHS = ["./fonts/dm-mono-400.430936c6c8.woff2", "./fonts/dm-sans-400.a298e7f5df.woff2", "./fonts/dm-sans-500.ae5023890d.woff2", "./fonts/dm-sans-700.c4a662e549.woff2"];
const FONT_URLS = new Set(FONT_PATHS.map(path => new URL(path, self.location.href).href));
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(FONT_PATHS)));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key.startsWith('technical-writing-fonts-') && key !== CACHE).map(key => caches.delete(key)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET' || !FONT_URLS.has(event.request.url)) return;
  event.respondWith(caches.open(CACHE).then(async cache => {
    const cached = await cache.match(event.request);
    if (cached) return cached;
    const response = await fetch(event.request);
    if (response.ok) await cache.put(event.request, response.clone());
    return response;
  }));
});
