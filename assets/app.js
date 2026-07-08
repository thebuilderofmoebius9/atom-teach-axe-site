(function(){
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
    card.textContent=pass?`ผ่านครับ: ถูก ${correct}/${quizzes.length} ข้อ เข้าใจแก่นบทนี้แล้ว`:`ยังควรทวนครับ: ถูก ${correct}/${quizzes.length} ข้อ ลองอ่าน Executive Brief แล้วตอบใหม่`;
    card.classList.toggle('score-good', pass);
    card.classList.toggle('score-warn', !pass);
  }
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
})();
