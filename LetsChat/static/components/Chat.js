class Chat extends React.Component{
  constructor(props){
    super(props);

    this.state = {
      chatSocket: new WebSocket('ws://127.0.0.1:8000/ws/chat/'+props.roomName+'/'),
      roomName: props.roomName,
      image:this.props.image,
      message: "",
      messages_: [],
    }
  }

  componentDidMount(){
    this.state.chatSocket.onopen = ()=>{
      console.log("socket is open");
    };

    this.state.chatSocket.onclose = ()=>{
      console.log("socek is closed");
    };

    this.state.chatSocket.onmessage = (event)=>{
      let data = JSON.parse(event.data);
      let message = data["message"];
      this.setState({
        messages_:[...this.state.messages_, message],
      })
      console.log(this.state.messages_);
    }

  }

  sendMessage = ()=>{
    let message = this.state.message;
    let image = this.state.image;
    this.setState({
      message: ''
    })

    this.state.chatSocket.send(JSON.stringify({
      "message":message,
      "image":image,
    }));
  }

  changeMessage = (event) => {
    let {value, name} = event.target;
    this.setState({
      [name]: value
    })

  }

  render(){
    let messages = this.state.messages_.map((value, index)=>{
      {value.message}
      return (
        <li key={index} className="media shadow-sm p-3 mb-5 bg-white rounded">
          <img src={value.image} className="align-self-center mr-3" width="20%" height="20%" alt="..." />
            <div className="media-body">
              <h5 className="mt-0">message</h5>
              <p className="mb-0">{value.message}</p>
            </div>
        </li>
      )
    });
    return(
      <div>
        <div className="card" style={{width:"100%",height:"40em"}}>
        <div className="card-header">
          Chat
        </div>
        <div className="card-body overflow-auto">
          <ul className="list-group list-group-flush overflow-auto">
            {messages}
          </ul>
        </div>
          <div className="card-footer">
            <input type="text" style={{width:"90%"}} name="message" value={this.state.message} onChange={this.changeMessage}/>
            <button onClick={this.sendMessage} style={{width:"10%"}}>Send</button>
          </div>
        </div>
      </div>
    )
  }
}
