console.log('hello')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'GET',
   url: `${url}data`,
    success: function(response){
        //console.log(response)
        const data = response.data
        data.forEach(el => {
            for(const [question, answers] of Object.entries(el)){
                console.log(question)
                console.log(answers)
            }
        })
    },
    error: function(error){
        console.log(error)
    }
})