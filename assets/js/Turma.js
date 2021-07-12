import CardCursos from './CardCursosHtml.js';

class Turma {
    constructor(titulo, texto, imagem, orientacao, horarioInicio, horarioFinal) {
        this.info = {
            titulo,
            texto,
            imagem,
            orientacao,
            horarioInicio,
            horarioFinal
        };
    }

    formatadorHorario(horarioInicial, horarioFinal){
        return `${horarioInicial} até ${horarioFinal}`;
    }

    appendBootstrapCard() {
        const editedHTML = CardCursos({ ...this.info, horario: this.formatadorHorario(this.info.horarioInicio, this.info.horarioFinal) });
        $("#turmas").append(editedHTML);
    }
}

export default Turma;
