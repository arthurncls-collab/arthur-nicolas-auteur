const button=document.querySelector(".menu-button");const nav=document.querySelector(".nav");button?.addEventListener("click",()=>{const open=nav.classList.toggle("open");button.setAttribute("aria-expanded",String(open))});nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.classList.remove("open");button?.setAttribute("aria-expanded","false")}));const year=document.querySelector("#year");if(year)year.textContent=String(new Date().getFullYear());

const rssContainer=document.querySelector("#rss-episodes");
if(rssContainer){
  fetch("podcast-feed.json",{cache:"no-store"})
    .then(r=>{if(!r.ok)throw new Error("feed");return r.json()})
    .then(data=>{
      const episodes=Array.isArray(data.episodes)?data.episodes.slice(0,4):[];
      if(!episodes.length)throw new Error("empty");
      rssContainer.innerHTML="";
      for(const ep of episodes){
        const article=document.createElement("article");
        article.className="rss-episode";
        const date=ep.published?new Date(ep.published):null;
        const dateLabel=date&&!Number.isNaN(date.valueOf())?date.toLocaleDateString("fr-FR",{day:"2-digit",month:"long",year:"numeric"}):"";
        const safeTitle=ep.title||"Épisode";
        const safeDescription=ep.description||"";
        article.innerHTML=`
          ${dateLabel?`<time datetime="${ep.published}">${dateLabel}</time>`:""}
          <h3></h3>
          ${safeDescription?"<p></p>":""}
          ${ep.audio?`<audio controls preload="none" src="${ep.audio}">Votre navigateur ne prend pas en charge le lecteur audio.</audio>`:""}
          ${ep.link?`<a class="episode-link" href="${ep.link}" target="_blank" rel="noreferrer">Ouvrir l'épisode →</a>`:""}
        `;
        article.querySelector("h3").textContent=safeTitle;
        const p=article.querySelector("p");if(p)p.textContent=safeDescription;
        rssContainer.appendChild(article);
      }
    })
    .catch(()=>{
      rssContainer.innerHTML='<p class="rss-loading">Les épisodes restent disponibles dans le lecteur Spotify ci-dessus.</p>';
    });
}
