var birthDate = new Date('1991-05-18');
var ageInMilliseconds = Date.now() - birthDate.getTime();
var ageDate = new Date(ageInMilliseconds);
var age = Math.abs(ageDate.getUTCFullYear() - 1970);
document.getElementById('age').textContent = age;