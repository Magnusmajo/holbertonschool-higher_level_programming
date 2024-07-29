document.addEventListener('DOMContentLoaded', function () {
  const addButton = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');

  addButton.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});
