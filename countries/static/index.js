document.getElementById('country').addEventListener('change', onSelectCountry)

function createRow({ casos_confirmados,
  mortes,
  recuperados }) {
  if (casos_confirmados && mortes && recuperados) {
    return `
    <tr class="bg-blue-800 bg-opacity-20">
      <td class="px-20 py-2">${casos_confirmados}</td>
      <td class="px-20 py-2">${mortes}</td>
      <td class="px-20 py-2">${recuperados}</td>
    </tr>`
  } else return ''
}

function onSelectCountry(event) {
  let request = new XMLHttpRequest();
  request.open('GET', `/country/${event.target.value}`);
  request.responseType = 'json';

  request.onload = function () {
    const list = document.getElementById('list');
    list.innerHTML = ''
    let row = {}

    request.response.covidData.forEach((item) => {
      if (!row.data || new Date(row.data) < new Date(item.data)) {
        row = item;
      }
    })

    list.innerHTML += createRow(row)
  };

  request.send();
}