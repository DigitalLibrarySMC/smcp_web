console.log("Hello world quiz")
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
let timer;
let displaySeconds;
let displayMinutes;
let timez;



const activateTimer = (time) => {
  if (time.toString().length < 2) {
    timerBox.innerHTML = `<b>0${time}:00</b>`
  }else{
    timerBox.innerHTML = `<b>${time}:00</b>`
  }

  let minutes = time -  1
  let seconds  = 60


  timer = setInterval(()=>{
    seconds--
    if (seconds<0){
      seconds = 59
      minutes --
    }
    if (minutes.toString().length<2){
      displayMinutes = '0'+minutes
    }else{
      displayMinutes = minutes
    }
    if (seconds.toString().length<2){
      displaySeconds = '0' + seconds
    } else{
      displaySeconds = seconds
    }
    if (minutes === 0 && seconds === 0){
      timerBox.innerHTML = "<b>00:00</b>"
      setTimeout(()=>{
        clearInterval(timer)
        alert('Time over')
        sendData()
      }, 500)
    }

    timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
  }, 1000)

}


$.ajax({
  type: 'GET',
  url: `${url}data`,
  success: function(response){
    //console.log(response)
    const data = response.data
    data.forEach(el => {
      for (const[question, answers] of Object.entries(el) ){
        quizBox.innerHTML += `
           <hr>
           <div class="mb-2">
             <b>${question}</b>
           </div>
        `
        answers.forEach(answer=>{
          quizBox.innerHTML +=`
            <div>
               <input type="radio" class="answer" id="${question}-${answer}" name="${question}" value="${answer}">
               <label for="${question}">${answer}</label>
            </div>
          `
        })
      }
    })
    timez = response.time*60
    activateTimer(response.time)
  },
  error: function(error){
    console.log(error)
  }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


const sendData = () =>{
  const elements = [...document.getElementsByClassName('answer')]
  const data = {}
  data['csrfmiddlewaretoken']=csrf[0].value
  const takenMinutes = parseInt(displayMinutes);
  const takenSeconds = parseInt(displaySeconds);
  const takenTimeInSeconds = takenMinutes*60 + takenSeconds;
  data['takentime'] = timez - takenTimeInSeconds;
  elements.forEach(el=>{
    if (el.checked) {
      data[el.name] = el.value
    } else{
      if (!data[el.name]) {
        data[el.name] = null
      }
    }
  })

  $.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,
    success: function(response){
     // console.log(response)
      const results  = response.results
      console.log(results)
      quizForm.classList.add('d-none')

      scoreBox.innerHTML =`${response.passed ?  'Congratulations' : 'Ups...:('}Your result is ${response.score.toFixed(2)}%`

      results.forEach(res=>{
        const resDiv = document.createElement("div")
        for (const [question, resp] of Object.entries(res)){

          resDiv.innerHTML += question
          const cls = ['container', 'p-3', 'text-light', 'h6']
          resDiv.classList.add(...cls)

          if (resp=='not answered'){
            resDiv.innerHTML += '-not answered'
            resDiv.classList.add('bg-danger')
          }
          else{
            const answer = resp['answered']
            const correct  = resp['correct_answer']

            if  (answer == correct) {
              resDiv.classList.add('bg-success')
              resDiv.innerHTML += ` answered: ${answer}`
            }else {
              resDiv.classList.add('bg-danger')
              resDiv.innerHTML += ` | correct answer: ${correct}`
              resDiv.innerHTML += ` | answered: ${answer}`
            }
          }
        }
       // const body = document.getElementsByTagName('BODY')[0]
        resultBox.append(resDiv)
      })
      clearInterval(timer);
    },
    error: function(error){
      console.log(error)
    }
  })
}

quizForm.addEventListener('submit', e=>{
  e.preventDefault()

  sendData()
})