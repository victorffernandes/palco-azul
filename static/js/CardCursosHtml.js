export default ({ id, titulo, texto, imagem }) => {
    const cssSide = id % 2 === 1 ? 'align-self-start' : 'align-self-end';
    const imgDiv = `<div class='col-md-4 align-self-center'>
        <img src='/${imagem}' class='img-fluid' alt='...'>
    </div>`

    return `<div class='mb-3 ${cssSide}' style='max-width: 700px;' id='${titulo}'>
    <div class='row g-0'>
        ${ id % 2 === 1 && imgDiv || ''}
        <div class='col-md-8'>
          <div class='card-body'>
            <h5 class='card-title'>${titulo}</h5>
            <p class='card-text'>${texto}</p>
          </div>
        </div>
        ${ id % 2 === 0 && imgDiv || ''}
      </div>
  </div>`
};