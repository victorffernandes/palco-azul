import Turma from './Turma.js'

$.ajax({
    url: '/alunos/turmas',
    type: 'get',
    success: function (object) {
        let turmasObjects = object.map(t => new Turma(t.nome, t.descricao, t.image, t.id));
        turmasObjects = turmasObjects.sort((a, b) => +a.info.id - +b.info.id);
        console.log(turmasObjects)
        const cards = turmasObjects.map(t => t.appendBootstrapCard());
    },
    error: function (jquery, textStatus, error) {
        alert('Ocorreu um erro', error);
    }
});
