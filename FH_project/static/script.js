document.getElementById("js-open-modal-btn").addEventListener("click",function(){
    document.getElementById("js-my-modal").classList.add("open")
})

document.getElementById("js-close-my-modal").addEventListener("click",function(){
    document.getElementById("js-my-modal").classList.remove("open")
})

document.getElementById("js-register-btn").addEventListener("click",function(){
    document.getElementById("js-my-modal").classList.add("open");
    document.getElementById("js-my-modal-login").classList.remove("open");
    document.getElementById("js-my-modal-login").classList.add("close");
    document.getElementById("js-my-modal-register").classList.add("open");
})

document.getElementById("js-close-my-modal-register").addEventListener("click",function(){
    document.getElementById("js-my-modal").classList.remove("open");
    document.getElementById("js-my-modal-register").classList.remove("open");
    document.getElementById("js-my-modal-login").classList.remove("close");
})

document.getElementById("js-next-step-btn").addEventListener("click",function(){
    document.getElementById("js-first-reg-page").classList.add("close");
    document.getElementById("js-second-reg-page").classList.add("open");
    document.getElementById("js-step").classList.add("close");
    document.getElementById("js-step2").classList.add("open");
})

document.getElementById("js-prev-step-btn").addEventListener("click",function(){
    document.getElementById("js-first-reg-page").classList.remove("close");
    document.getElementById("js-second-reg-page").classList.remove("open");
    document.getElementById("js-step").classList.remove("close");
    document.getElementById("js-step2").classList.remove("open");
})


const input = document.querySelectorAll('input');
for (let elem of input)
{
    elem.addEventListener('input', () => {
        if (elem.value !== '') {
            elem.classList.add('input_filled');
        } else {
            elem.classList.remove('input_filled');
        }
    })
}

const yesRadio = document.getElementById('yes');
const noRadio = document.getElementById('no');
const additionalBlock = document.getElementById('additional-block');

function handleChoiceChange() {
    if (yesRadio.checked) {
        additionalBlock.style.display = 'block';
    }
    else {
        additionalBlock.style.display = 'none';
    }
}

yesRadio.addEventListener('change', handleChoiceChange);
noRadio.addEventListener('change', handleChoiceChange);

// Функция для обновления скрытого поля с продуктами
function updateAllergiesInput() {
    const stringItems = document.querySelectorAll(".string-item");
    const allergies = Array.from(stringItems).map(item => item.textContent.trim());
    document.getElementById("allergiesInput").value = allergies.join(", ");
}

// Функция для отображения поля ввода текста
function showInput() {
    const inputField = document.getElementById("newInput");
    const addButton = document.getElementById("newButton");
    inputField.classList.add("open");
    addButton.classList.add("open");
}

function closeInput() {
    const inputField = document.getElementById("newInput");
    const addButton = document.getElementById("newButton");
    inputField.classList.remove("open");
    addButton.classList.remove("open");
}

// Добавляем обработчик события click к контейнеру
const container = document.getElementById("textInputContainer");
container.addEventListener("click", function(event) {
  if (event.target.id === "newButton") {
    const inputField = document.getElementById("newInput");
    const inputValue = inputField.value.trim();
    if (inputValue) {
      addString(inputValue);
      inputField.value = "";
      closeInput(); 
    }
  }
});

// Добавляем обработчик события click для кнопки "добавить продукт / группу продуктов"
const showInputButton = document.getElementById("showInputButton");
showInputButton.addEventListener("click", showInput);
