import CardCursos from './CardCursosHtml.js';

class Turma {
    constructor(titulo, texto, imagem, id) {
        this.info = {
            titulo,
            texto,
            imagem,
            id,
        };
    }

    appendBootstrapCard() {
        const editedHTML = CardCursos({ ...this.info});
        $("#turmas").append(editedHTML);
    }
}

export default Turma;
