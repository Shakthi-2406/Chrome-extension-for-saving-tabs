let lead = []
const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const tabBtn = document.getElementById("tab-btn")
const deleteBtn = document.getElementById("delete-btn")
const ulEl = document.getElementById("ul-el")


const leadFromLocal = JSON.parse(localStorage.getItem("leadStore"))


if (leadFromLocal)
{
    lead = leadFromLocal
    render(lead)
}


tabBtn.addEventListener("click", function ()
{
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        lead.push(tabs[0].url)
        localStorage.setItem("leadStore",JSON.stringify(lead))
        render(lead)
    })
})


function render(lead)
{
        let li = ""
        for(let i=0; i< lead.length; i++)
        { 
            li += `<li> 
                <a href="${lead[i]}" target="_blank">
                  ${lead[i]} 
                </a>
            </li>`
        }
        ulEl.innerHTML = li
}


inputBtn.addEventListener("click",function()
{
    if (inputEl.value != "")
    {
        lead.push(inputEl.value)
        inputEl.value= ""
        localStorage.setItem("leadStore",JSON.stringify(lead))
        render(lead)
    }
})


deleteBtn.addEventListener("dblclick",function()
{
        localStorage.clear()
        ulEl.innerHTML = ""
        lead = []
})








// localStorage.setItem("shak","sweety")
// console.log(localStorage.getItem("shak"))
// localStorage.clear()
// inputEl.value = localStorage.getItem("shak")