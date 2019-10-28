let pageAry = ["home_page", "dish_page", "table_page", "order_page", "dish_edit_page",
    "dish_create_page", "create_table", "edit_table"]

function toggleDiv(div) {
    pageAry.forEach((page) => {
        document.getElementById(page).style.display = "none";
    });
    if (div == "dish_page") {
        loadAllDish()
    } else if (div == "table_page") {
        laodAllTable();
    }
    document.getElementById(div).style.display = "block";
}

function loadAllDish() {
    eel.getAllDish()((dishes) => {
        console.info(dishes)
        let str = ""
        dishes.forEach((dish) => {
            str += `
                        <tr class="text-white">
                            <td>${dish[0]}</td>
                            <td>${dish[1]}</td>
                            <td>${dish[2]}</td>
                            <td>
                                <button class="btn btn-warning btn-sm" onclick="editDish(${dish[0]})">Edit</button>
                                <button class="btn btn-danger btn-sm" onclick="deleteDish(${dish[0]})">Delete</button>
                            </td>
                        </tr>
                        `;
        });
        document.getElementById("all_dishes_show").innerHTML = str;
    })
}

function laodAllTable() {
    eel.getAllTable()((tables) => {
        let str = "";
        tables.forEach((table) => {
            str += `
                <tr class="text-white">
                    <td>${table[0]}</td>
                    <td>${table[1]}</td>
                    <td>
                        <button class="btn ${table[2] == 0 ? "btn-secondary" : "btn-success"} btn-sm">
                            ${table[2] == 0 ? "Engage" : "Bill Out"}
                        </button>
                    </td>
                    <td>
                        <button class="btn btn-warning btn-sm" onclick="editTable(${table[0]})">Edit</button>
                        <button class="btn btn-danger btn-sm" onclick="deleteTable(${table[0]})">Delete</button>
                    </td>
                </tr>
            `;
        })
        document.getElementById("all_table_show").innerHTML = str;
    });
}

function editTable(id) {
    eel.getTableById(id)((table) => {
        document.getElementById("edit_table_id").value = table[0]
        document.getElementById("edit_table_name").value = table[1]
        toggleDiv("edit_table")
    });
}

function updateTable(){
   let id = document.getElementById("edit_table_id").value;
   let name =  document.getElementById("edit_table_name").value;

    eel.updateTable(id,name)((data)=>{
        toggleDiv("table_page")
    })
}

function editDish(id) {
    eel.getDishByid(id)((dish) => {
        document.getElementById("edit_dish_id").value = dish[0];
        document.getElementById("edit_dish_name").value = dish[1];
        document.getElementById("edit_dish_price").value = dish[2];
    });
    toggleDiv("dish_edit_page");
}

function deleteTable(id) {
    eel.deleteTable(id)((data) => {
        toggleDiv("table_page")
    })
}

function addDish() {
    let name = document.getElementById("create_dish_name").value;
    let price = document.getElementById("create_dish_price").value;

    eel.insertDish(name, price)((data) => {
        toggleDiv("dish_page");
    })
}

function deleteDish(id) {
    eel.deleteDish(id)((data) => {
        toggleDiv("dish_page");
    });
}

function updateDish() {
    let id = document.getElementById("edit_dish_id").value;
    let name = document.getElementById("edit_dish_name").value;
    let price = document.getElementById("edit_dish_price").value;

    eel.updateDish(id, name, price)((data) => {
        toggleDiv("dish_page");
    })
}

function createTable() {
    let name = document.getElementById("create_table_name").value;
    eel.createTable(name)((data) => {
        toggleDiv("table_page");
    })
}

toggleDiv("home_page")