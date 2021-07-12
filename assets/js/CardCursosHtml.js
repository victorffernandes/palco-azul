export default ({ orientacao, titulo, texto, imagem, horario }) => {
    const cssSide = orientacao === 'left' ? 'align-self-start' : 'align-self-end';
    const imgDiv = `<div class='col-md-4 align-self-center'>
        <img src='${imagem}' class='img-fluid' alt='...'>
        <p><b>Horário: </b>${horario}</p>
    </div>`

    return `<div class='mb-3 ${cssSide}' style='max-width: 700px;' id='adulto'>
    <div class='row g-0'>
        ${ orientacao === 'left' && imgDiv || ''}
        <div class='col-md-8'>
          <div class='card-body'>
            <h5 class='card-title'>${titulo}</h5>
            <p class='card-text'>${texto}</p>
          </div>
        </div>
        ${ orientacao === 'right' && imgDiv || ''}
      </div>
  </div>`
};