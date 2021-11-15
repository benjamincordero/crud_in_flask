app = new Vue({
  el:'#app',
  data:{
  },
  methods:{
    deletePost(post_id){
      Swal.fire({
        title: 'Está seguro?',
        text: "No podrá revertir esta acción",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText:'Cancelar',
        confirmButtonText: 'Sí, continuar!'
      }).then(async (result) => {
        if (result.isConfirmed) {
          form = new FormData();
          form.append('post_id', post_id);
          var data = await fetch(url_delete, {
            method:'POST',
            body:form
          });
          var datajson = await data.json()
         if(datajson.success){
           Swal.fire(
            'Eliminado!',
            'El post ha sido eliminado.',
            'success'
          );  
          document.getElementById('post_id_'+post_id).remove()
         }else{
          Swal.fire(
            'Ha ocurrido un error!',
            'El post no ha sido eliminado.',
            'error'
          );
         }
          
        }
      })
      
    },
  },
  created(){

  }
})
