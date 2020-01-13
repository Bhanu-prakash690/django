class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      roomName: this.props.roomName,
      image: this.props.image,
    }
  }

  async componentDidMount(){

  }

  render(){

    console.log(this.state.roomName);
    return(
      <div>
        <Chat roomName={this.state.roomName} image={this.state.image}/>
      </div>
    )
  }

}
