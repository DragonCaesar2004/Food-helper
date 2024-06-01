
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

function addString(inputValue) {
    if (inputValue) {
        // const stringList = document.getElementById("stringList");
        const newStringItem = document.createElement("div");
        const stringItemName = document.createElement("div");
        stringItemName.classList.add("string-item-block");
        const stringItemAmount = document.createElement("div");
        stringItemAmount.classList.add("string-item-block");
        const stringItemType = document.createElement("div");
        stringItemType.classList.add("string-item-block");

        const newForm = document.createElement("form");
        newForm.classList.add("form-of-types");
        const newSelectDiv = document.createElement("div");
        newSelectDiv.classList.add("select-type");
        newSelectDiv.setAttribute("data-state", "");
        const newSelectTitle = document.createElement("div");
        newSelectTitle.classList.add("select-type-title");
        newSelectTitle.setAttribute("data-default", "Option 0");
        const newSelectContent = document.createElement("div");
        newSelectContent.classList.add("select-type-content");

        const newSelectInput1 = document.createElement("input");
        const newSelectInput2 = document.createElement("input");
        const newSelectInput3 = document.createElement("input");

        newSelectInput1.classList.add("select-type-input");
        newSelectInput1.setAttribute("type", "radio");
        newSelectInput1.setAttribute("name", "singleSelect");
        newSelectInput1.setAttribute("id", "unit-kg");
        newSelectInput1.value = "kg";

        newSelectInput2.classList.add("select-type-input");
        newSelectInput2.setAttribute("type", "radio");
        newSelectInput2.setAttribute("name", "singleSelect");
        newSelectInput2.setAttribute("id", "unit-g");
        newSelectInput2.value = "g";

        newSelectInput3.classList.add("select-type-input");
        newSelectInput3.setAttribute("type", "radio");
        newSelectInput3.setAttribute("name", "singleSelect");
        newSelectInput3.setAttribute("id", "unit-piece");
        newSelectInput3.value = "piece";

        const newSelectInputLabel1 = document.createElement("label");
        const newSelectInputLabel2 = document.createElement("label");
        const newSelectInputLabel3 = document.createElement("label");

        newSelectInputLabel1.classList.add("select-type-label");
        newSelectInputLabel1.setAttribute("for", "unit-kg");
        newSelectInputLabel1.textContent = "кг";

        newSelectInputLabel2.classList.add("select-type-label");
        newSelectInputLabel2.setAttribute("for", "unit-g");
        newSelectInputLabel2.textContent = "г";

        newSelectInputLabel3.classList.add("select-type-label");
        newSelectInputLabel3.setAttribute("for", "unit-piece");
        newSelectInputLabel3.textContent = "шт";

        newSelectContent.appendChild(newSelectInput1);
        newSelectContent.appendChild(newSelectInputLabel1);
        newSelectContent.appendChild(newSelectInput2);
        newSelectContent.appendChild(newSelectInputLabel2);
        newSelectContent.appendChild(newSelectInput3);
        newSelectContent.appendChild(newSelectInputLabel3);

        newSelectTitle.textContent = "кг";
        newSelectDiv.appendChild(newSelectContent);
        newSelectDiv.appendChild(newSelectTitle);

        newForm.appendChild(newSelectDiv);

        newStringItem.classList.add("string-item");
        stringItemName.textContent = inputValue;

        // Создаем элемент для изображения крестика (svg)
        const newIcon = document.createElement("img");
        newIcon.setAttribute("src", "img/close-btn-list.svg"); // Укажите путь к файлу с изображением крестика
        newIcon.classList.add("cross-icon");
        newIcon.addEventListener("click", function() {
            // stringList.removeChild(newStringItem); // Удаляем строку при клике на крестик
        });

        const itemAmount = document.createElement("input");
        itemAmount.classList.add("inputbox-hw");
        stringItemAmount.appendChild(itemAmount);

        newStringItem.appendChild(stringItemName);
        newStringItem.appendChild(stringItemAmount);
        newStringItem.appendChild(newForm);
        newStringItem.appendChild(newIcon); // Добавляем иконку крестика к строке
        // stringList.insertBefore(newStringItem, stringList.firstChild);

        // Обработчики событий для нового элемента select
        const selectSingle = newSelectDiv;
        const selectSingle_title = selectSingle.querySelector('.select-type-title');
        const selectSingle_labels = selectSingle.querySelectorAll('.select-type-label');

        // Toggle menu
        selectSingle_title.addEventListener('click', () => {
            if ('active' === selectSingle.getAttribute('data-state')) {
                selectSingle.setAttribute('data-state', '');
            } else {
                selectSingle.setAttribute('data-state', 'active');
            }
            selectSingle_title.classList.add("close");
        });

        // Close when click to option
        for (let i = 0; i < selectSingle_labels.length; i++) {
            selectSingle_labels[i].addEventListener('click', (evt) => {
                selectSingle_title.textContent = evt.target.textContent;
                selectSingle.setAttribute('data-state', '');
                selectSingle_title.classList.remove("close");
            });
        }

        // document.getElementById("newInput").value = "";
    }
}


// Функция для отображения поля ввода текста
function showInput() {
    // Создаем элемент input
    // const inputField = document.getElementById("newInput");
    // Создаем кнопку для добавления введенного текста
    // const addButton = document.getElementById("newButton");
    inputField.classList.add("open");
    addButton.classList.add("open");
}

function closeInput() {
    // const inputField = document.getElementById("newInput");
    // Создаем кнопку для добавления введенного текста
    // const addButton = document.getElementById("newButton");
    inputField.classList.remove("open");
    addButton.classList.remove("open");
}

// Добавляем обработчик события click к контейнеру
// const container = document.getElementById("textInputContainer");
// container.addEventListener("click", function(event) {
//   // Проверяем, что клик произошел на кнопке "Добавить"
//   if (event.target.id === "newButton") {
//     const inputField = document.getElementById("newInput");
//     const inputValue = inputField.value.trim();
//     if (inputValue) {
//       addString(inputValue);
//       // Очищаем поле ввода после добавления
//       inputField.value = "";
//       // Скрываем поле ввода и кнопку
//       closeInput(); 
//     }
//   }
// });

// Добавляем обработчик события click для кнопки "добавить съеденную пищу"
// const showInputButton = document.getElementById("showInputButton");
// showInputButton.addEventListener("click", showInput);

const addMealButton = document.getElementById("addMealTimeButton");
addMealButton.addEventListener("click", ()=> {
    addMealButton.classList.add("close");
    const addMealForm = document.getElementById("addMealForm");
    addMealForm.classList.add("open");
})

const setTimeBtn = document.getElementById("setTimeButton");
setTimeBtn.addEventListener("click", ()=> {
    setTimeBtn.classList.add("close");
    const addTimeForm = document.getElementById("addTimeForm");
    addTimeForm.classList.add("open");
})

function toggleInputMenu(){
    const selectSingle = document.querySelector('.__select');
    const selectSingle_title = selectSingle.querySelector('.__select__title');
    const selectSingle_labels = selectSingle.querySelectorAll('.__select__label');

    // Toggle menu
    selectSingle_title.addEventListener('click', () => {
    if ('active' === selectSingle.getAttribute('data-state')) {
        selectSingle.setAttribute('data-state', '');
    } else {
        selectSingle.setAttribute('data-state', 'active');
    }
    });

    // Close when click to option
    for (let i = 0; i < selectSingle_labels.length; i++) {
    selectSingle_labels[i].addEventListener('click', (evt) => {
        selectSingle_title.textContent = evt.target.textContent;
        selectSingle.setAttribute('data-state', '');
    });
    }
}

toggleInputMenu();

document.addEventListener('DOMContentLoaded', () => {
    const addMealButton = document.getElementById('addMealButton');
    const foodAddInfo = document.getElementById('foodAddInfo');
    // const stringList = document.getElementById('stringList');
    // const newInput = document.getElementById('overallResult');
    // const newButton = document.getElementById('newButton');
    const addMealForm = document.getElementById('addMealForm');
    const addTimeForm = document.getElementById('addTimeForm');
    const setTimeButton = document.getElementById('setTimeButton');
    const submitTimeButton = document.querySelector('.submit-time-btn');
    const foodInfoBlock = document.querySelector('.food-add-info'); // Контейнер для новых блоков информации
    const resultsBtn = document.getElementById('resultsBtn'); // Кнопка для отправки формы
    const chatBlock = document.getElementById('chatBlock');

    // Открытие формы для добавления приёма пищи
    addMealButton.addEventListener('click', () => {
        foodAddInfo.style.display = 'block';
        chatBlock.classList.add("close");
    });

    // Добавление употребленных продуктов в список
    // newButton.addEventListener('click', () => {
    //     // const inputValue = newInput.value.trim();
    //     if (inputValue) {
    //         const newStringItem = document.createElement('div');
    //         newStringItem.classList.add('string-item');
    //         newStringItem.textContent = inputValue;
    //         // stringList.appendChild(newStringItem);
    //         // newInput.value = '';
    //     }
    // });

    // Обработка времени приема пищи
    submitTimeButton.addEventListener('click', () => {
        const timeInput = document.getElementById('time').value;
        if (timeInput) {
            setTimeButton.textContent = timeInput;
        }
    });

    // Обработка клика по кнопке для отправки формы
    resultsBtn.addEventListener('click', () => {
        const mealType = addMealForm.querySelector('input[name="singleSelect"]:checked').nextElementSibling.textContent;
        const mealTime = setTimeButton.textContent;
        //const overallResult = newInput.textContent;

        // Создаем новый блок с информацией о приёме пищи
        const newFoodInfo = document.createElement('div');
        newFoodInfo.classList.add('food-info-block');

        const mealTypeDiv = document.createElement('div');
        const mealTypeSpan = document.createElement('span');
        mealTypeSpan.textContent = mealType;
        mealTypeDiv.appendChild(mealTypeSpan);

        const mealTimeDiv = document.createElement('div');
        const mealTimeP = document.createElement('p');
        mealTimeP.textContent = mealTime;
        mealTimeDiv.appendChild(mealTimeP);

        const foodItemsDiv = document.createElement('div');
        const foodItemsP = document.createElement('p');
        //foodItemsP.textContent = overallResult;
        //foodItemsDiv.appendChild(foodItemsP);
        
        const detailButtonDiv = document.createElement('div');
        const detailButton = document.createElement('button');
        detailButton.classList.add('main-links');
        detailButton.textContent = 'Подробнее';
        detailButtonDiv.appendChild(detailButton);

        const editButtonDiv = document.createElement('div');
        const editButton = document.createElement('button');
        editButton.classList.add('main-btns');
        const editImg = document.createElement('img');
        editImg.setAttribute('src', 'img/pencil.svg');
        editButton.appendChild(editImg);
        editButtonDiv.appendChild(editButton);

        newFoodInfo.appendChild(mealTypeDiv);
        newFoodInfo.appendChild(mealTimeDiv);
        newFoodInfo.appendChild(foodItemsDiv);
        newFoodInfo.appendChild(detailButtonDiv);
        newFoodInfo.appendChild(editButtonDiv);

        foodInfoBlock.appendChild(newFoodInfo);

         // Скрываем форму после добавления информации
         foodAddInfo.style.display = 'none';
         chatBlock.classList.remove("close");
         addMealForm.reset();
         addTimeForm.reset(); // Сброс формы времени
        //  stringList.innerHTML = '';
         setTimeButton.textContent = '00:00';
 
         // Сброс выбранного типа приема пищи к первому элементу
         const firstOption = addMealForm.querySelector('input[name="singleSelect"]');
         if (firstOption) {
             firstOption.checked = true;
             const selectTitle = addMealForm.querySelector('.__select__title');
             if (selectTitle) {
                 selectTitle.textContent = firstOption.nextElementSibling.textContent;
             }
         }
    });
});



const dateElement = document.getElementById('currentDate');
const currentDate = new Date();
const formattedDate = currentDate.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
});
dateElement.textContent = formattedDate;

document.getElementById('recovery-password-btn').addEventListener('click', function() {
    event.preventDefault();
    const email = document.getElementById('email').textContent;
    fetch('/api/recovery-password/', {
        method: 'POST',
        body: JSON.stringify({
            mail_for_recovery: email,
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
      .then(data => {
          if (data.message) {alert(data.message);
          } else if (data.error) {
              alert(data.error);
          }
      });
});


//Кнопка редактирования, сохранения, отмены сохранения
document.getElementById('edit-info-btn').addEventListener('click', function() {
    document.querySelectorAll('.personal_info_subblock span').forEach(span => {
        span.style.display = 'none';
    });
    document.querySelectorAll('.edit-input').forEach(input => {
        input.style.display = 'inline-block';
    });

    document.getElementById('email-input').value = document.getElementById('email').textContent;
    document.getElementById('gender-input').value = document.getElementById('gender').textContent;
    document.getElementById('date_of_birth-input').value = document.getElementById('date_of_birth').textContent;
    document.getElementById('height-input').value = document.getElementById('height').textContent;
    document.getElementById('weight-input').value = document.getElementById('weight').textContent;
    document.getElementById('vegan_vegetarian-input').value = document.getElementById('vegan_vegetarian').textContent;
    document.getElementById('allergies-input').value = document.getElementById('allergies').textContent;
    document.getElementById('goal-input').value = document.getElementById('goal').textContent;


    document.getElementById('edit-info-btn').style.display = 'none';
    document.getElementById('save-info-btn').style.display = 'inline-block';
    document.getElementById('cancel-edit-btn').style.display = 'inline-block';
});

document.getElementById('cancel-edit-btn').addEventListener('click', function() {
    document.querySelectorAll('.edit-input').forEach(input => {
        input.style.display = 'none';
    });
    document.querySelectorAll('.personal_info_subblock span').forEach(span => {
        span.style.display = 'inline-block';
    });
    document.getElementById('edit-info-btn').style.display = 'inline-block';
    document.getElementById('save-info-btn').style.display = 'none';
    document.getElementById('cancel-edit-btn').style.display = 'none';
});

document.getElementById('save-info-btn').addEventListener('click', function() {
    document.querySelectorAll('.edit-input').forEach(input => {
        const id = input.id.replace('-input', '');
        document.getElementById(id).textContent = input.value;
        input.style.display = 'none';
    });
    document.querySelectorAll('.personal_info_subblock span').forEach(span => {
        span.style.display = 'inline-block';
    });
    document.getElementById('edit-info-btn').style.display = 'inline-block';
    document.getElementById('save-info-btn').style.display = 'none';
    document.getElementById('cancel-edit-btn').style.display = 'none';
});