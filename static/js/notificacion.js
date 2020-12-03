//Titulo de la notificación
Push.create("DWY4101- DuocUC", {

    //Texto del cuerpo de la notificación
    body: "Ejemplo de mensaje de notificación.",

    icon: "https://img.icons8.com/plasticine/200/000000/reddit.png", //Icono de la notificación
    timeout: 6000, //Tiempo de duración de la notificación


    onClick: function() {
        //Función que se cumple al realizar clic cobre la notificación
        window.location = "https://www.duoc.cl"; //Redirige a la siguiente web
        this.close(); //Cierra la notificación
    },
});