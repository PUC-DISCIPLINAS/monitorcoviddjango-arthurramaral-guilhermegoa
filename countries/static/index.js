const select = document.getElementById('country');
const list = document.getElementById('list');

select.addEventListener('change', onSelectCountry)

function getGlobal() {
  select.disable = true;

  const pulseSize = 1;
  list.innerHTML = '';

  for (let i = 0; i < pulseSize; i++) list.innerHTML += createRow('-', { casos_confirmados: '-', mortes: '-', recuperados: '-' }, true)

  let request = new XMLHttpRequest();
  request.open('GET', '/stats');
  request.responseType = 'json';

  request.onload = function () {
    list.innerHTML = ''

    request.response.countries.forEach((pais) => {
      let row;

      request.response.covidData.forEach((item) => {
        if (pais.id === item.pais_id && (!row || (new Date(row.data) < new Date(item.data)))) {
          row = item;
        }
      })

      if (row)
        list.innerHTML += createRow(pais.nome, row)
    })
  };

  request.send();
}

function createRow(pais, { casos_confirmados,
  mortes,
  recuperados }, loading) {
  return `
    <tr class="bg-blue-800 bg-opacity-20 ${loading && 'animate-pulse'}">
      <td class="px-20 py-2">${pais || ''}</td>
      <td class="px-20 py-2">${casos_confirmados == 0 ? 0 : casos_confirmados || ''}</td>
      <td class="px-20 py-2">${mortes == 0 ? 0 : mortes || ''}</td>
      <td class="px-20 py-2">${recuperados == 0 ? 0 : recuperados || ''}</td>
    </tr>`
}

function onSelectCountry(event) {
  const value = event.target.value;
  if (value) {
    const splitValue = value.split(':', 2);
    const idDoPais = splitValue[0];
    const nomeDoPais = splitValue[1];

    let request = new XMLHttpRequest();
    request.open('GET', `/country/${idDoPais}`);
    request.responseType = 'json';

    request.onload = function () {
      list.innerHTML = ''
      let row = {}

      request.response.covidData.forEach((item) => {
        if (!row.data || new Date(row.data) < new Date(item.data)) {
          row = item;
        }
      })

      list.innerHTML += createRow(nomeDoPais, row)
    };

    request.send();
  } else getGlobal()
}

getGlobal()