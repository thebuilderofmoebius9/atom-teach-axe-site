(function(){
  const storeKey='atom-teach-axe-progress-v2';
  const readProgress=()=>{
    try{return JSON.parse(localStorage.getItem(storeKey)||'{}')}catch{return {}}
  };
  const writeProgress=(p)=>{
    try{localStorage.setItem(storeKey,JSON.stringify(p))}catch{}
  };
  function allCards(){return [...document.querySelectorAll('[data-lesson-card]')];}
  function refreshHomeProgress(){
    const progress=readProgress();
    const cards=allCards();
    const done=cards.filter(c=>progress[c.dataset.slug]).length;
    const pct=cards.length?Math.round(done/cards.length*100):0;
    const xp=document.getElementById('home-xp');
    if(xp) xp.textContent=pct+'%';
    cards.forEach(card=>{
      const pill=card.querySelector('[data-complete-for]');
      const ok=!!progress[card.dataset.slug];
      card.classList.toggle('complete',ok);
      if(pill){pill.textContent=ok?'ผ่านแล้ว +XP':'ยังไม่ผ่าน'; pill.classList.toggle('done',ok);}
    });
  }
  function filterCards(q){
    q=(q||'').trim().toLowerCase();
    allCards().forEach(card=>{
      const hay=card.dataset.search||'';
      card.hidden=!!q && !hay.includes(q);
    });
  }
  function initHome(){
    const search=document.getElementById('quest-search');
    if(search) search.addEventListener('input',()=>filterCards(search.value));
    document.querySelectorAll('[data-filter]').forEach(btn=>btn.addEventListener('click',()=>{
      const key=btn.dataset.filter.toLowerCase();
      if(search) search.value=key;
      filterCards(key);
      document.querySelector('.quest-zone')?.scrollIntoView({behavior:'smooth',block:'start'});
    }));
    const random=document.getElementById('random-quest');
    if(random) random.addEventListener('click',()=>{
      const visible=allCards().filter(c=>!c.hidden);
      const pick=visible[Math.floor(Math.random()*visible.length)]||allCards()[0];
      const link=pick&&pick.querySelector('a[href]');
      if(link) location.href=link.href;
    });
    const reset=document.getElementById('reset-progress');
    if(reset) reset.addEventListener('click',()=>{
      writeProgress({});
      refreshHomeProgress();
      reset.textContent='ล้างแล้ว';
      setTimeout(()=>reset.textContent='ล้าง XP',1000);
    });
    refreshHomeProgress();
  }
  function updateScore(){
    const quizzes=[...document.querySelectorAll('[data-quiz]')];
    const answered=quizzes.filter(q=>q.dataset.answered==='true');
    const correct=answered.filter(q=>q.dataset.ok==='true').length;
    const card=document.getElementById('score-card');
    if(!card) return;
    if(answered.length<quizzes.length){
      card.textContent=`ตอบแล้ว ${answered.length}/${quizzes.length} ข้อ · ถูก ${correct} ข้อ`;
      return;
    }
    const pass=correct>=4;
    card.textContent=pass?`ผ่านครับ: ถูก ${correct}/${quizzes.length} ข้อ ได้รับ XP และเข้าใจแก่นบทนี้แล้ว`:`ยังควรทวนครับ: ถูก ${correct}/${quizzes.length} ข้อ ลองอ่าน Mission Brief แล้วตอบใหม่`;
    card.classList.toggle('score-good', pass);
    card.classList.toggle('score-warn', !pass);
    const section=document.querySelector('[data-lesson-slug]');
    if(pass&&section){
      const progress=readProgress();
      progress[section.dataset.lessonSlug]={score:correct,total:quizzes.length,passedAt:new Date().toISOString()};
      writeProgress(progress);
      card.insertAdjacentHTML('beforeend','<span class="xp-burst"> +XP</span>');
      setTimeout(()=>card.querySelector('.xp-burst')?.remove(),1200);
    }
  }
  function initQuiz(){
    document.addEventListener('click', (event)=>{
      const btn=event.target.closest('.choice');
      if(!btn) return;
      const quiz=btn.closest('[data-quiz]');
      quiz.querySelectorAll('.choice').forEach(b=>{b.classList.remove('good','bad'); b.setAttribute('aria-pressed','false');});
      const ok=btn.dataset.correct==='true';
      btn.classList.add(ok?'good':'bad');
      btn.setAttribute('aria-pressed','true');
      quiz.dataset.answered='true';
      quiz.dataset.ok=String(ok);
      const feedback=quiz.querySelector('.feedback');
      feedback.textContent=btn.dataset.feedback || (ok?'ถูกครับ':'ยังไม่ใช่ครับ');
      feedback.classList.toggle('ok', ok);
      feedback.classList.toggle('no', !ok);
      updateScore();
    });
    updateScore();
  }
  function initReveal(){
    const els=[...document.querySelectorAll('.section,.lesson-card,.card,.term-card')];
    if(!('IntersectionObserver' in window)){els.forEach(e=>e.classList.add('in-view'));return;}
    const io=new IntersectionObserver(entries=>{
      entries.forEach(ent=>{if(ent.isIntersecting){ent.target.classList.add('in-view');io.unobserve(ent.target);}});
    },{threshold:.08});
    els.forEach(e=>io.observe(e));
  }
  initHome();
  initQuiz();
  initReveal();
})();
