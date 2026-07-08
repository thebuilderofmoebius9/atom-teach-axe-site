function mark(btn, ok){
  document.querySelectorAll('.choice').forEach(b=>b.classList.remove('good','bad'));
  btn.classList.add(ok?'good':'bad');
  const f=document.getElementById('feedback');
  if(f){f.textContent=ok?'ถูกครับ: ใช้ TF-IDF หา salience ก่อน แล้วค่อยกลับไปอ่านหลักฐานจริงด้วย FTS5':'ยังไม่สุดครับ: วิธีนี้ไม่ตอบว่า “หัวข้อไหนเด่นเมื่อเทียบกับช่วงอื่น” ได้ดีเท่า TF-IDF';}
}
