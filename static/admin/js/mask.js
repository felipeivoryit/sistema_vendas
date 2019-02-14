$(document).ready(function(){

    /********** form cliente ***********/
    
    /* Máscara input data nascimento - form cliente */
    $('#id_data_nascimento').mask('00/00/0000', {placeholder: "__/__/____"});
    
    /* Máscara input cpf - form cliente */    
    $('#id_cpf').mask('000.000.000-00', {placeholder: "___.___.___.___-__"}, {reverse: true});
    
    /********** form funcionário ***********/
    
    /* Máscara input data nascimento - form funcionário */
    $('#id_data_nascimento').mask('00/00/0000', {placeholder: "__/__/____"});
    
    /* Máscara input remuneração - form funcionário */
    $('#id_remuneracao').mask('000.000.000.000.000,00');
    
});
