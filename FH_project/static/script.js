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

function addString(inputValue) {
    if (inputValue) {
        const stringList = document.getElementById("stringList");
        const newStringItem = document.createElement("div");
        newStringItem.classList.add("string-item");
        newStringItem.textContent = inputValue;

        // Создаем элемент для изображения крестика (svg)
        const newIcon = document.createElement("img");
        newIcon.setAttribute("src", "{% static 'img/close-btn-list.svg' %}"); // Укажите путь к файлу с изображением крестика
        newIcon.classList.add("cross-icon");
        newIcon.addEventListener("click", function() {
            stringList.removeChild(newStringItem); // Удаляем строку при клике на крестик
            updateAllergiesInput(); // Обновляем значение скрытого поля
        });
        
        newStringItem.appendChild(newIcon); // Добавляем иконку крестика к строке
        stringList.insertBefore(newStringItem, stringList.firstChild);

        updateAllergiesInput();

        document.getElementById("newInput").value = "";
    }
}

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

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/api/login/', {
        method: 'POST',
        body: JSON.stringify({
            username: formData.get('username'),
            password: formData.get('password')
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
      .then(data => {
          if (data.access) {
              localStorage.setItem('token', data.access);
              window.location.href = '/profile/';
          }
      });
});

document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => { data[key] = value });
    
    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            window.location.href = '';
        } else {
            response.json().then(data => {
                console.error('Error:', data);
            });
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});