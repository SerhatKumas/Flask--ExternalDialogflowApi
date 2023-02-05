function fetch_intent_list(){
    let counter = 1;
    fetch('/all-intents-page-info').then(response => response.json()).then(function(intent_data){
        for(let i = 0; i < intent_data.length; i+=2){
            let tr_object = document.createElement("tr");
            let th_object = document.createElement("th");
            th_object.setAttribute("scope", "row");
            th_object.innerHTML = (counter).toString() ;
            counter++;
            let td_object_1 = document.createElement("th");
            td_object_1.innerHTML = intent_data[i] ;
            let td_object_2 = document.createElement("th");
            td_object_2.innerHTML = intent_data[i+1];
            tr_object.appendChild(th_object);
            tr_object.appendChild(td_object_1);
            tr_object.appendChild(td_object_2);
            document.getElementById("information-table").appendChild(tr_object);
        }
    });
}