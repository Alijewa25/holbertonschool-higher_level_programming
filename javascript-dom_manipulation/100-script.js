#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#add_item').addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item';
    document.querySelector('.my_list').appendChild(li);
  });

  document.querySelector('#remove_item').addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function() {
    document.querySelector('.my_list').innerHTML = '';
  });
});
