import re,html
photos=[l for l in open('photo-list.txt').read().splitlines() if l.startswith('- gbp')]
items=[]
for l in photos:
    f,d=l[2:].split(': ',1); cat=f.split('-')[1].replace('.jpg','')
    cat={'beforeafter':'repair'}.get(cat,cat)
    items.append((f,d,cat))
labels={'repair':'Body Repair','paint':'Paint','car':'Finished Rides','shop':'The Shop'}
gal='\n'.join(f'<figure class="g-item reveal" data-cat="{c}"><img src="assets/gallery/{f}" alt="{html.escape(d)}" loading="lazy"><figcaption>{html.escape(d)}</figcaption></figure>' for f,d,c in items)
wip=['gbp-beforeafter-01.jpg','gbp-repair-03.jpg','gbp-repair-10.jpg','gbp-repair-11.jpg','gbp-repair-12.jpg','gbp-paint-02.jpg','gbp-repair-06.jpg','gbp-repair-04.jpg']
dmap={f:d for f,d,c in items}
wiphtml='\n'.join(f'<div class="wip-card"><img src="assets/gallery/{f}" alt="{html.escape(dmap[f])}" loading="lazy"><span>{html.escape(dmap[f])}</span></div>' for f in wip)
reviews=[("Louie Ponce","7 months ago","Mario was the most humble and kind man around. The work he did on our Tesla was incredible and we were impressed how well he did. He took a little over a day to knock it out and we were really happy with the results. The value of his work was worth more than what he charged, so huge plus!"),
("Shanissa F","3 months ago","I am so impressed by the work and timeliness with the repairs for my car. I brought in my Mazda CX-5 for a quote and was followed up shortly after with a detailed copy of what the cost for repairs would be. It was very competitive compared …"),
("Beth Clarke","3 years ago","Mario and his staff are amazing. They explained everything to me so that I understood exactly what was wrong with my vehicle. They serviced my car quickly and at a great price. I would highly recommend them."),
("Dennis Martin","7 months ago","Mario & his crew are the best I've dealt with EVER! Great work from a good man at a great price!"),
("Logan Ruiz","3 years ago","Great experience working with Mario!! He's very nice and does outstanding work. We were quoted at half the price of another shop in town who was trying to add on services we didn't need. Our vehicle was also ready sooner than expected."),
("Jim Lyon","","Mario did an excellent job in repairing the auto body damage to my car. Can't even tell where it was damaged, very reasonable price too!"),
("Scott Woodhams","4 years ago","Great guy, quality work, and reasonable. Highly recommended. I have had several vehicles painted/repaired here, and happy each time."),
("Cameron Cooper","5 years ago","When searching for an A+ body shop, look no further than Mario! Not only does Mario perform top-notch work, and I mean great work! He also is a great guy personally, and always takes the time personally with his clients…"),
("Sitting Bull","","Mario is remarkable! Talented and efficient, as well as thoughtful. He is one-of-a-kind.")]
rev='\n'.join(f'<article class="review reveal"><div class="stars">★★★★★</div><p>“{html.escape(t)}”</p><footer><strong>{n}</strong><span>{w+" · " if w else ""}Google review</span></footer></article>' for n,w,t in reviews)
filters=''.join(f'<button data-filter="{k}">{v}</button>' for k,v in labels.items())
t=open('template.html').read().replace('{{GALLERY}}',gal).replace('{{WIP}}',wiphtml).replace('{{REVIEWS}}',rev).replace('{{FILTERS}}',filters).replace('{{COUNT}}',str(len(items)))
open('index.html','w').write(t)
