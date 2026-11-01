import sys
from playwright.sync_api import sync_playwright
url=sys.argv[1];tag=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for n,vp in [('desktop',{'width':1440,'height':900}),('mobile',{'width':390,'height':844})]:
        pg=b.new_page(viewport=vp);pg.goto(url,wait_until='load');pg.wait_for_timeout(800)
        H=pg.evaluate('document.documentElement.scrollHeight');i=0;y=0;blank=[]
        while y<H:
            pg.screenshot(path=f'screenshots/scrollcheck/{tag}-{n}-{i:02d}.png')
            r=pg.evaluate("""()=>{let h=0;document.querySelectorAll('.reveal').forEach(e=>{const b=e.getBoundingClientRect();if(b.bottom>0&&b.top<innerHeight&&getComputedStyle(e).opacity<0.5)h++});
             const im=[...document.images].filter(e=>{const b=e.getBoundingClientRect();return b.bottom>0&&b.top<innerHeight&&!e.complete}).length;return [h,im]}""")
            if r[0] or r[1]: blank.append((i,r))
            for _ in range(6): pg.mouse.wheel(0,vp['height']/6);pg.wait_for_timeout(120)
            pg.wait_for_timeout(500);i+=1;y=pg.evaluate('scrollY')+0;H=pg.evaluate('document.documentElement.scrollHeight')
            if y+vp['height']>=H and i>1 and pg.evaluate('scrollY+innerHeight>=document.documentElement.scrollHeight-2'):
                pg.screenshot(path=f'screenshots/scrollcheck/{tag}-{n}-{i:02d}.png');break
        print(n,'steps',i,'hidden/unloaded at steps:',blank)
    b.close()
