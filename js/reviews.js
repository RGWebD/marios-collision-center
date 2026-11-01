/* Live Google reviews (optional).
   1) Create a Google Cloud API key with "Places API (New)" enabled, restricted to this site's domain.
   2) Paste it below and set PLACE_ID (find it at https://developers.google.com/maps/documentation/places/web-service/place-id).
   Until both are set, the static real reviews already in the page are shown. */
const GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY';
const PLACE_ID = 'YOUR_PLACE_ID';
(async()=>{
  if(GOOGLE_API_KEY.startsWith('YOUR_')||PLACE_ID.startsWith('YOUR_'))return;
  try{
    const r=await fetch(`https://places.googleapis.com/v1/places/${PLACE_ID}`,{headers:{'X-Goog-Api-Key':GOOGLE_API_KEY,'X-Goog-FieldMask':'rating,userRatingCount,reviews,googleMapsUri'}});
    if(!r.ok)return;const p=await r.json();
    if(p.rating)document.getElementById('g-rating').textContent=p.rating.toFixed(1);
    if(p.userRatingCount)document.getElementById('g-count').textContent=p.userRatingCount;
    if(p.googleMapsUri)document.querySelector('.g-badge').href=p.googleMapsUri;
    const good=(p.reviews||[]).filter(v=>v.rating>=4&&v.text);if(!good.length)return;
    const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
    const g=document.getElementById('review-grid');
    g.innerHTML=good.map(v=>`<article class="review reveal"><div class="stars">${'★'.repeat(v.rating)}</div><p>“${esc(v.text.text)}”</p><footer><strong>${esc(v.authorAttribution?.displayName||'Google user')}</strong><span>${esc(v.relativePublishTimeDescription||'')} · Google review</span></footer></article>`).join('');
    g.querySelectorAll('.reveal').forEach(el=>window.observeReveal?observeReveal(el):el.classList.add('in'));
  }catch(e){}
})();
