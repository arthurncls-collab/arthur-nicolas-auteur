const button=document.querySelector(".menu-button");
const nav=document.querySelector(".nav");
button?.addEventListener("click",()=>{
  const open=nav.classList.toggle("open");
  button.setAttribute("aria-expanded",String(open));
});
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{
  nav.classList.remove("open");
  button?.setAttribute("aria-expanded","false");
}));
const year=document.querySelector("#year");
if(year) year.textContent=String(new Date().getFullYear());

const rssContainer=document.querySelector("#rss-episodes");
if(rssContainer){
  fetch("podcast-feed.json",{cache:"no-store"})
    .then(r=>{
      if(!r.ok) throw new Error("feed");
      return r.json();
    })
    .then(data=>{
      const episodes=Array.isArray(data.episodes)?data.episodes.slice(0,3):[];
      if(!episodes.length) throw new Error("empty");
      rssContainer.innerHTML="";

      for(const ep of episodes){
        const article=document.createElement("article");
        article.className="rss-episode"+(ep.image?"":" no-image");

        if(ep.image){
          const img=document.createElement("img");
          img.className="rss-thumb";
          img.src=ep.image;
          img.alt="";
          img.loading="lazy";
          article.appendChild(img);
        }

        const content=document.createElement("div");
        content.className="rss-content";

        if(ep.published){
          const date=new Date(ep.published);
          if(!Number.isNaN(date.valueOf())){
            const time=document.createElement("time");
            time.dateTime=ep.published;
            time.textContent=date.toLocaleDateString("fr-FR",{day:"2-digit",month:"long",year:"numeric"});
            content.appendChild(time);
          }
        }

        const title=document.createElement("h3");
        title.textContent=ep.title||"Épisode";
        content.appendChild(title);

        if(ep.description){
          const p=document.createElement("p");
          p.textContent=ep.description;
          content.appendChild(p);
        }

        if(ep.audio){
          const audio=document.createElement("audio");
          audio.controls=true;
          audio.preload="none";
          audio.src=ep.audio;
          content.appendChild(audio);
        }

        if(ep.link){
          const a=document.createElement("a");
          a.className="episode-link";
          a.href=ep.link;
          a.target="_blank";
          a.rel="noreferrer";
          a.textContent="Ouvrir l'épisode →";
          content.appendChild(a);
        }

        article.appendChild(content);
        rssContainer.appendChild(article);
      }
    })
    .catch(()=>{
      rssContainer.innerHTML='<p class="rss-loading">Les épisodes restent disponibles dans le lecteur Spotify ci-dessus.</p>';
    });
}
