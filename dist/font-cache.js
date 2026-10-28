// Optional enhancement: the site still works when service workers are unavailable.
if ('serviceWorker' in navigator && window.isSecureContext) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./font-sw.js', {scope: './'}).catch(() => {
      // First-party font URLs still use the browser's normal HTTP cache.
    });
  });
}
