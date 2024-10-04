const { useState, useEffect } = require("react");

function App(){
  const [content,setContent] = useState("")
  const [message,setMessage] = useState("")
  const [messages,setMessages] = useState([])
  const [user,setUser] = useState("noname")
  const [pnum,setPnum] = useState(1)
  const [plast,setPlast] = useState(1)

  const getMsgs = (num) => {
    getPlast()
    setPnum(num)
    fetch('http://localhost:8000/api/msgs/'+num)
    .then(response => response.json())
    .then(data => {
      setMessages(data)
    });
  }
  const getUser = () => {
    fetch('http://localhost:8000/api/usr/')
    .then(response => response.json())
    .then(data => {
      setUser(data.value)
    });
  }
  const getPlast = () => {
    fetch('http://localhost:8000/api/plast/')
    .then(response => response.json())
    .then(data => {
      setPlast(data.value)
    });
  }
  const doChange = (e) => {
    setContent(e.target.value)
  }
  const doAction = (e) => {
    const data = {
      content:content,
    }
    fetch('http://localhost:8000/api/post/', {
      method: 'POST',
      headers: {},
      body: JSON.stringify(data),
    })
    .then(response => response.text())
    .then(data => {
      getPlast()
      getMsgs(1)
      if(data.result == "OK"){
        setContent("")
        setMessage("メッセージを投稿しました!")
      }
    });
  }
  const doGood = (e) => {
    fetch('http://localhost:8000/api/good/' + e.target.id)
    .then(response => response.text())
    .then(res => {
      getMsgs(pnum)
      console.log(res)
      if(res.result == "OK"){
        setMessage("goodしました!")
      }else{
        setMessage("すでにgoodしています")
      }
    })
  }
  const onFirst = () => {
    getMsgs(1)
  }
  const onPrev = () => {
    const p = pnum - 1 <= 1 ? 1 : pnum - 1
    getMsgs(p)
  }
  const onNext = () => {
    const p = pnum + 1 >= plast ? plast : pnum + 1
    getMsgs(p)
  }
  const onLast = () => {
    getMsgs(plast)
  }

  useEffect(() => {
    getMsgs(1)
    getUser()
  },[])

  return(
    <div className="App">
      <h1 className="display-4 text-primary">SNS</h1>
      <p className="fs-3"> logined: {user}</p>
      <div>
        {message != "" && (
          <div className="alert alert-primary alert-dismissible fade show" role="alert">
            <p>{message}</p>
            <button type="button" className="btn-close" data-bs-dismiss="alert"></button>
          </div>
        )}
        <div className="content">
          <textarea className="form-control" onChange={doChange} value={content}></textarea>
          <button className="btn btn-primary" onClick={doAction}>Post</button>
          <table className="table mt-3">
            <tr>
              <th>Messages</th>
              {messages.map(msg => (
                <tr key={msg.id}>
                  <td>
                    <p className="fs-4 my-0">
                      {msg.fields.content}
                    </p>
                    <p className="my-0 text-end">
                      <span className="fs-5">
                        ({msg.fields.owner_name})
                      </span>
                      <span className="fs-6">
                        {msg.fields.pub_date}
                      </span>
                    </p>
                    <p className="mt-1 fs-6 text-end">
                      <span className="h6 text-primary">
                        good={msg.fields.good_count}
                      </span>
                      <span className="float-right">
                        <span className="mx-2">
                          {console.log(msg.fields)}
                          <button className="btn btn-outline-primary py-0 px-1" id={msg.pk} onClick={doGood}>Good</button>
                        </span>
                      </span>
                    </p>
                  </td>
                </tr>
              ))}
            </tr>
          </table> 
          <ul className="pagination justifuy-content-center">
            <li className="page-item">
              <p className="page-link" onClick={onFirst}>&laquo; First</p>
            </li>
            <li className="page-item">
              <p className="page-link" onClick={onPrev}>&laquo; Prev</p>
            </li>
            <li className="page-item">
              <p className="page-link" onClick={onNext}>&raquo;Next</p>
            </li>
            <li className="page-item">
              <p className="page-link" onClick={onLast}>&raquo;Last</p>
            </li>
          </ul>
        </div>
      </div>
      <hr />
    </div>
  )
}
export default App;