const email_input_fields = document.querySelectorAll("div.input__field.email > input")
const password_input_fields = document.querySelectorAll("div.input__field.password > input")

console.log(email_input_fields)
console.log(password_input_fields)

email_input_fields.forEach(input => {
  input.addEventListener("input", handleChangeEmail.bind(input))
})

password_input_fields.forEach(input_pw => {
  input_pw.addEventListener("input", handleChangePassword.bind(input_pw))
})

function handleChangeEmail(e){
  const email_regEx = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/
  let input_val = e.target.value
  if(input_val.match(email_regEx)){
    console.log("valid")
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#95D995"
    console.log()
    
  }else{
    console.log("invalid")
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#F3797E"
  }

  if(!input_val){
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#6441a5"
  }

}

function handleChangePassword(e){
  const passwd_regEx = /^([a-zA-Z0-9 _-]+)$/
  let input_val = e.target.value
  console.log(input_val)

  if(input_val.match(passwd_regEx)){
    console.log("valid")
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#95D995"
    console.log()
    
  }else{
    console.log("invalid")
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#F3797E"
  }

  if(!input_val){
    e.target.parentElement.querySelector(".line").style.backgroundColor = "#6441a5"
  }

}
