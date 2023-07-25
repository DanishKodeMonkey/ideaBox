function submitIdea(){
    const idea = document.getElementById("ideaInput").value;

    //Create JSON object with data from ideaInput
    const data ={
        idea:idea
    };

    //send the idea to backend using Fetch API
    fetch('/submit_idea',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    })
    ,then(Response =>{
        if(Response.ok){
            return Response.json();
        } else{
            throw new Error('Failed to submit data');
        }
    })
    ,then(data=>{
        alert(data.message);
        document.getElementById("ideaInput").value = '';
    })
    .catch(error => {
        // Show an error message to the user
        alert(error.message);
    });
}