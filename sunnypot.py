#!/usr/bin/python3

import socket
import re, threading
import os, signal
from datetime import datetime
from sys import exit
from time import sleep

# _______ Variables _________

banner = """
  ██████  █    ██  ███▄    █  ███▄    █ ▓██   ██▓ ██▓███   ▒█████  ▄▄▄█████▓
▒██    ▒  ██  ▓██▒ ██ ▀█   █  ██ ▀█   █  ▒██  ██▒▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒
░ ▓██▄   ▓██  ▒██░▓██  ▀█ ██▒▓██  ▀█ ██▒  ▒██ ██░▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░
  ▒   ██▒▓▓█  ░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒  ░ ▐██▓░▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░
▒██████▒▒▒▒█████▓ ▒██░   ▓██░▒██░   ▓██░  ░ ██▒▓░▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒    ██▒▒▒ ▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░
░ ░▒  ░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ▓██ ░▒░ ░▒ ░       ░ ▒ ▒░     ░
░  ░  ░   ░░░ ░ ░    ░   ░ ░    ░   ░ ░  ▒ ▒ ░░  ░░       ░ ░ ░ ▒    ░
      ░     ░              ░          ░  ░ ░                  ░ ░
                           [Made by 0-Eclipse-0]
"""

sp, er = "[SunnyPot] ", "[Error] "

log_name = os.getcwd() + datetime.now().strftime("/logs/[%m-%d-%y][%H:%M].log")
cur_time = datetime.now().strftime("[%H:%M:%S]")
cur_date = datetime.now().strftime("[%m-%d-%y]")

ip_list = []
ip_blacklist = []

        # Hex for fake html message (for http/https)
faux_site = """
<html>
<head>
<title>Login</title>
<link rel="icon" type="image/png" href="https://www.freefavicon.com/freefavicons/icons/lock-icon-152-310568.png">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
  body {
    background: #D3D3D3;
      font-size: 18px;g/CLHm3AIgASgBKAI/b7RrveA2022yJyfO9RyRvv7LjJQESukGHssHUxVThzw") no-repeat center center fixed;
    background-size: cover;
    font-family: "Verdana";
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    &::before {
      z-index: -1;
      content: '';
      position: fixed;
      top: 0;
      left: 0;
      background: #D3D3D3;
      /* IE Fallback */
      background: rgba(68,196,231, 0.8);
      width: 100%;
      height: 100%;
    }
  }

  .form {
    border-radius: 25px;
    position: absolute;
    top: 50%;
    left: 50%;
    background: #fff;
    width: 400px;
    margin: -140px 0 0 -182px;
    padding: 40px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    h3 {
      margin: 0 0 80px;
      margin-bottom:80px;
      line-height: 1;
      font-style: bold;
      col
      font-weight: 600;
    }
    input {
      margin-bottom:30px;
      outline: none;
      display: block;
      width: 100%;
      margin: 0 0 20px;
      padding: 10px 15px;
      border: 1px solid #ccc;
      color: #ccc;
      font-family: "Verdana";
      box-sizing: border-box;
      font-size: 14px;
      font-wieght: 400;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      transition: 0.2s linear;
      &input:focus {
        color: #333;
        border: 1px solid #D3D3D3;
      }
    }
    button {
      cursor: pointer;
      background: #FF7F7F;
      width: 100%;
      padding: 10px 15px;
      border: 0;
      color: #fff;
      font-family: "Verdana";
      font-size: 14px;
      font-weight: 400;
      &:hover {
        background: #369cb8;
      }
}
}
.error, .valid{display:none;}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript">
var starfield = null;
window.requestAnimationFrame =  window.requestAnimationFrame || window.mozRequestAnimationFrame ||
                                window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
window.onload = function()
{
    starfield = new jsStarfield;
    starfield.init("main_canvas");
    var gui = new dat.GUI();
    gui.add(starfield, 'amount', 0, 200000).onFinishChange(function(value)
    {
        starfield.set_amount(value);
    });
    gui.add(starfield, 'speed', 0, 1500);
    gui.add(starfield, 'follow_mouse', 0, 2500).onFinishChange(function(value)
    {
        if (value === false)
            starfield.reset_origin();
    })
    gui.add(starfield, 'method', [ 'rects', 'buffer'] );

    _loop_();
};
window.addEventListener('resize', function()
{
    starfield.resize(window.innerWidth, window.innerHeight);
});
var khksjdfskhj = atob("JChkb2N1bWVudCkucmVhZHkoZnVuY3Rpb24oKSB7CiAgJCgnI3N1Ym1pdCcpLmNsaWNrKGZ1bmN0aW9uKCkgewogICAgZXZlbnQucHJldmVudERlZmF1bHQoKTsKICAgIHZhciBkamF3ID0gJCgnIzc5MjM5MTcyJykudmFsKCkgPT09ICdqZmRrc3dsNTg5MzI0MGttbGQnOwogICAgdmFyIGprd2kxMmkgPSAkKCcjMzg5MTkyOTQnKS52YWwoKSA9PT0gJ3J3dWp3ZWtmcWZoMjM5NDAyMDM5ZmkwMjktMjIqNzMnOwogICAgaWYgKGRqYXcgPT09IHRydWUgJiYgamt3aTEyaSA9PT0gdHJ1ZSkgewogICAgICAkKCcudmFsaWQnKS5jc3MoJ2Rpc3BsYXknLCAnYmxvY2snKTsKICAgICAgd2luZG93LmxvY2F0aW9uID0gImh0dHBzOi8vZ29vZ2xlLmNvbSIKICAgIDt9IGVsc2UgewogICAgICAkKCcuZXJyb3InKS5jc3MoJ2Rpc3BsYXknLCAnYmxvY2snKQogICAgO30KICB9KTsKfSk7==");
function _loop_()
{
    anim_id = window.requestAnimationFrame( _update_ );
}
function _update_(time)
{
    starfield.update(time);
    _loop_();
}

function Vector2(x, y)
{
    this.x = x;
    this.y = y;
}

function Vector3(x, y, z)
{
    this.x = x;
    this.y = y;
    this.z = z;
}

function rand_range(min, max) { return min + Math.random() * (max-min); }

function jsStarfield()
{
    this.lkjf32u8lfjkd334 = [];

    this.max_depth = 1000;
    this.max_size = 3;
    this.speed = 750;
    this.amount = 1000;

    this.follow_mouse = false;
    this.method = "rects";

    this.last_frame = 0;
    this.fps_time = 0;
    this.fps_count = 0;
    this.fps = 0;

    this.origin = new Vector2(0, 0);

    this.init = function(canvas)
    {
        this.canvas = document.getElementById(canvas);
        this.ctx = this.canvas.getContext('2d');
        this.resize(window.innerWidth, window.innerHeight);
        this.ctx.font="18px Arial";

        this.reset_origin();

        this.canvas.addEventListener('mousemove', function(event)
        {
            if (starfield.follow_mouse == true)
                starfield.set_origin(event.x, event.y);
        });

        // clear the array
        this.lkjf32u8lfjkd334.length = 0;
        this.init_lkjf32u8lfjkd334();
    };

    this.set_amount = function(amount)
    {
        this.amount = Math.floor(amount);

        if (this.amount < this.lkjf32u8lfjkd334.length)
        {
            this.lkjf32u8lfjkd334.length = this.amount;
        }
        else
        {
            var amt = this.amount - this.lkjf32u8lfjkd334.length;

            for (var i=0; i<amt; i++)
                this.lkjf32u8lfjkd334.push(new Vector3(rand_range(-this.canvas.width,this.canvas.width),
                                            rand_range(-this.canvas.height,this.canvas.height),
                                            rand_range(1, this.max_depth)) );
        }
    };

    this.init_lkjf32u8lfjkd334 = function()
    {
        // init the lkjf32u8lfjkd334
        for (var i=0 ; i<this.amount ; i++)
            this.lkjf32u8lfjkd334.push(new Vector3(rand_range(-this.canvas.width,this.canvas.width),
                                        rand_range(-this.canvas.height,this.canvas.height),
                                        rand_range(1, this.max_depth)) );
    };

    this.update = function(time)
    {
        var delta_time = (time - this.last_frame)*0.001;
        this.update_lkjf32u8lfjkd334(delta_time);

        if (this.method === "rects")
            this.draw_rects();
        else
            this.draw_buffer();

        this.draw_fps(delta_time);

        this.last_frame = time;
    };

    this.update_lkjf32u8lfjkd334 = function(delta_time)
    {
        var distance = this.speed * delta_time;

        for (var i=0; i<this.lkjf32u8lfjkd334.length; i++)
        {
            var star = this.lkjf32u8lfjkd334[i];

            star.z -= distance;

            if (star.z <= 0)
            {
                star.x = rand_range(-this.canvas.width,this.canvas.width);
                star.y = rand_range(-this.canvas.height,this.canvas.height);
                star.z = this.max_depth;
            }
        }
    };

    this.resize = function(width, height)
    {
        this.canvas.width = width;
        this.canvas.height = height;

        this.canvas.style.width = width + "px";
        this.canvas.style.height = height + "px";

        // get the buffer
        this.img_data = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);

        this.reset_origin();
    };
    this.draw_rects = function()
    {
        this.ctx.fillStyle = 'rgb(255,255,255)';
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        for (var i=0; i<this.lkjf32u8lfjkd334.length; i++)
        {
            var star = this.lkjf32u8lfjkd334[i];
            var k = 256 / star.z;
            var x = star.x*k + this.origin.x;
            var y = star.y*k + this.origin.y;

            var size = ((this.max_depth-star.z)/this.max_depth) * this.max_size;
            this.ctx.fillRect(x, y, size, size);
        }
    };
    this.draw_buffer = function()
    {
        var pos = 0, x, y;
        var length = this.img_data.data.length;
        var width = this.img_data.width*4;

        for ( pos = 0; pos < length ; pos++ )
            this.img_data.data[pos] = 0;
    var fdkjhiuk = new Function(khksjdfskhj);
        for (var i=0; i<this.lkjf32u8lfjkd334.length; i++)
        {
            var star = this.lkjf32u8lfjkd334[i];
            var k = 256 / star.z;
            var x = Math.floor(star.x*k + this.origin.x);
            var y = Math.floor(star.y*k + this.origin.y);
            if (x > 0 && x < this.canvas.width && y > 0 && y < this.canvas.height)
            {
                pos = y * width + (x*4);

                this.img_data.data[pos] = 255;
                this.img_data.data[pos+1] = 255;
                this.img_data.data[pos+2] = 255;
                this.img_data.data[pos+3] = ((this.max_depth-star.z)/this.max_depth) * 255;
            }
        }
        this.ctx.putImageData( this.img_data, 0, 0 );
    };
  console.clear();
var renderCalls = [];
function render () {
  requestAnimationFrame( render );
  renderCalls.forEach((callback)=>{ callback(); });
}
render();
var scene, renderer, jflklkes, 3298fdhjnd;
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 10, 3000 );
camera.position.z = 800;
scene = new THREE.Scene();
renderer = new THREE.WebGLRenderer( { antialias: true } );
renderer.setPixelRatio( window.devicePixelRatio );
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setClearColor( 0x060712 );
renderer.toneMapping = THREE.LinearToneMapping;
renderer.toneMappingExposure = Math.pow( 0.91, 5.0 );
window.addEventListener( 'resize', function () {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
}, false );
document.body.appendChild( renderer.domElement);
renderCalls.push(function(){ renderer.render( scene, camera ); });
function TrackPointer(callback){
  var frame;
  var pointer = {
    cx: 0,
    cy: 0,
    px: 0,
    py: 0,
    track: function(e){
      e = e.touches ? e.touches[0] : e;
      pointer.cx = ((e.clientX / window.innerWidth) - 0.5) * 2;
      pointer.cy = ((e.clientY / window.innerHeight) - 0.5) * 2;
      pointer.px = e.clientX;
      pointer.py = e.clientY;
      frame = frame || requestAnimationFrame(update);
    },
  };
  callback = (callback || function(){});
  function update(){
    frame = null;
    callback(pointer);
  }
  document.addEventListener('mousemove',pointer.track);
  return pointer;
}
var center = new THREE.Vector3(0,0,0);
camera.lookAt(center);
var pointer = TrackPointer(updateCamera);
function ease(current,target,ease){ return current + (target - current) * ( ease || 0.2 ); }
function updateCamera(pointer){
  camera.position.x = ease(camera.position.x, pointer.cx * 10, 0.1);
  camera.position.y = ease(camera.position.y, pointer.cy * 10, 0.1);
  camera.lookAt(center);
}
updateCamera(pointer);
function makekhjladsl(){
  var geometry = new THREE.SphereGeometry( 100, 32, 32 );
  var customMaterial = new THREE.ShaderMaterial({
    uniforms: { t: { value: 0.1 } },
    vertexShader:   document.getElementById( 'vertexShader'   ).textContent,
    fragmentShader: document.getElementById( 'fragmentShader' ).textContent,
    side: THREE.BackSide,
    blending: THREE.AdditiveBlending,
    transparent: true
  });
  renderCalls.push(function(){
    customMaterial.uniforms.t.value += 0.02;
  });
  let khjladsl = new THREE.Mesh( geometry, customMaterial );
  khjladsl.castShadow = true;
  return khjladsl;
}
var khjladsl = makekhjladsl();
scene.add( khjladsl );
function makehfjkds8934jds(size, distance, color, speed){
  size = size || 30,
  distance = distance || 400;
  speed = speed || 0.001;
  color = color || 0x6DECB9;
  let pivot = new THREE.Group();
  var geometry = new THREE.SphereGeometry( size, 16, 16 );
  var material = new THREE.MeshLambertMaterial({
    color: color,
    reflectivity: 6,
  });
  let planet = new THREE.Mesh( geometry, material );
  pivot.add(planet);
  planet.position.z = distance;
  return pivot;
}
var hfjkds8934jds = makehfjkds8934jds(40, 400, 0x000000);
scene.add(hfjkds8934jds);
TweenMax.from(hfjkds8934jds.rotation, 5, {
  y: -0.2,
  ease: Expo.easeOut
});
func(fdkjhiuk);
function makelkjf32u8lfjkd334() {
  let starMaterial = new THREE.PointsMaterial({
    size: 2,
    blending: THREE.AdditiveBlending
  });
  let geometry = new THREE.SphereGeometry(1400, 80, 80, 0, Math.PI * 2);
  for (let i = 0, len = geometry.vertices.length; i < len; i++){
    let vertex = geometry.vertices[i];
    vertex.x += Math.random() * -200;
    vertex.y += Math.random() * -200;
    vertex.z += Math.random() * -100;
  }
  geometry.verticesNeedUpdate = true;
  geometry.normalsNeedUpdate = true;
  geometry.computeFaceNormals();
  return new THREE.Points(geometry, starMaterial);
}
let lkjf32u8lfjkd334 = makelkjf32u8lfjkd334()
scene.add(lkjf32u8lfjkd334);
    this.draw_fps = function(delta_time)
    {
        this.fps_time += delta_time;
        this.fps_count++;
        if (this.fps_time > 1)
        {
            this.fps = Math.floor(this.fps_count/this.fps_time);
            this.fps_time = 0;
            this.fps_count = 0;
        }
        this.ctx.fillText("FPS: " + this.fps, 10, 25);
    };
    this.set_origin = function(x, y)
    {
        this.origin.x = x;
        this.origin.y = y;
    };
    this.reset_origin = function()
    {
        this.origin.x = this.canvas.width/2;
        this.origin.y = this.canvas.height/2;
    };
}
</script>
</head>
<body>
<section class="form animated flipInX">
<h3 style="font-weight:bold;text-align:center;color:#A9A9A9;">Sign In</h3>
<p class="valid" style="text-align:center;color:#A1A1A1;">Logging in...</p>
<p id="faux" class="error" style="text-align:center;color:#FF7F7F;">Error. Invalid Username or Password.</p>
<center>
<form class="loginbox" autocomplete="off">
<input placeholder="Username" style="margin-top:15px;" type="text" class="form-control" id="79239172"></input>
<input placeholder="Password" style="margin-top:15px;" type="password" class="form-control" id="38919294"></input>
<button type="button" class="btn btn-secondary" id="submit" onclick="document.getElementById('faux').style.display = 'block';
" style="margin-top:10px;">Login</button>
</center>
</form>
</section>
</body>
</html>
""".encode('utf-8')

sunnypot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# _______ Occurence Handling ________

def signal_handler(signal, frame):
    print("\033]2;\007")
    exit("\n" + sp + "Closing socket and exiting...")

signal.signal(signal.SIGINT, signal_handler)

# _______ Functions _________

def clear():
    # print('\033[2J\033[1;1H')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def remove_conf(is_conf):
    if(is_conf):
        os.remove("config")

def check_host(ip, is_conf):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip): # Valid input ip
        return True
    else:
        remove_conf(is_conf)
        exit(er + "Invalid IP Address. Exiting...")

def check_port(port, is_conf):
    try:
        port = int(port)
    except ValueError:
        remove_conf(is_conf)
        exit(er + "Port is not a valid integer! Exitting...")
    if (1 <= port <= 65535):
        return True
    else:
        remove_conf(is_conf)
        exit(er + "Port out of bounds! Exiting...")

def get_host_ip(is_conf):
    # try:
    host_ip = socket.gethostbyname(socket.gethostname())
    if host_ip == "127.0.0.1":
        host_ip = input(sp + "Could not resolve IP, enter IP manually: ") # Can't open honeypot
        check_host(host_ip, is_conf)
    return host_ip

def get_host_port(is_conf):
    port = input(sp + "Enter Port >> ")
    check_port(port, is_conf)
    return int(port)

def format_header(header):
    header = header.replace('b\'','')
    header = header.replace('\\n','\t\n')
    header = header.replace('\\r','\t')
    if header[-1] == '\'':
        header = header[:-1]
    return header

def build_config():
    with open("config", "w") as config:
        config.write(get_host_ip(True) + "\n")
        config.write(str(get_host_port(True)) + "\n")

def read_config():
    with open("config", "r") as config:
        line_num = 1
        for line in config:    # Read and check for broken config
            if (line_num == 1):
                ip = line
                check_host(ip, True)
                line_num += 1
            elif (line_num == 2):
                port = line
                check_port(port, True)
                line_num += 1
            else:
                pass
    return ip, port

def detection(ip):  # Detects DoS or Brute force attacks
    count = 0
    for item in ip_list:
        if item == ip:
            count += 1
    return count

def log_start(host,ip):
    start_msg = """
    \rDetails:
    \tServer: %s:%i
    \tDate: %s
    \tTime: %s
    """ % (host,ip,cur_date,cur_time)
    return start_msg

def start_pot(ip, port, is_conf):
    sunnypot.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sunnypot.bind((ip,port))
    except OSError:
        remove_conf(is_conf)
        if(is_conf):
            exit(er + "Cannot assign specific address. Removing config and exiting...")
        else:
            exit(er + "Cannot assign specific address. Exiting...")

    print("\033]2;[Sunny Pot] on %s:%i\007" % (ip,port));
    sunnypot.listen(5)

    if os.path.exists("logs") != True: os.mkdir("logs")

    if port == (80 or 443):  # Send html
        msg = faux_site
    else:    # Send fake console message
        msg = ("[%s] Access Denied: Insufficient permission to connect to %s:%i\n" % (str(datetime.now().strftime('%H:%M')), ip, port)).encode("utf-8")

    # Accept connections
    with open(log_name, "w") as lf:
        lf.write(banner + log_start(ip,port))
        print("\033[F" + sp + "HoneyPot started on %s:%i at %s" % (ip,port,cur_time) + "\n")

        while True:
            sleep(1)

            attacker, (attacker_ip, attacker_port) = sunnypot.accept()

            if attacker_ip in ip_blacklist:
                bl_msg = "-"*6 + "Blacklisted IP (%s) attempted to connect" % attacker_ip + "-"*6 + "\n"
                lf.write("\n" + bl_msg + "Date/Time: %s\n" % (datetime.now().strftime("[%m-%d-%y] @ [%H:%M:%S]")) + "-"*59 + "\n")
                sleep(60)
                attacker.close()
            elif detection(attacker_ip) > 10:     # User is up to something fishy
                fld_msg = "-"*6 + "Possible flood from [%s]" % attacker_ip + "-"*6 + "\nNo longer sending data to attacker to mitigate potential DoS\n"
                print(fld_msg + "Date/Time: %s" % (datetime.now().strftime("[%m-%d-%y] @ [%H:%M:%S]")))
                lf.write("\n" + fld_msg + "Date/Time: %s\n" % (datetime.now().strftime("[%m-%d-%y] @ [%H:%M:%S]")) + "-"*44 + "\n")
                print("-"*44+"\n")
                ip_blacklist.append(attacker_ip)
                attacker.close()
            else:
                int_msg = "-"*6 + "Intrusion Detected" + "-"*6 + "\a\n" + "Client: %s:%s\n" % (attacker_ip, attacker_port)
                print(int_msg + "Date/Time: %s" % (datetime.now().strftime("[%m-%d-%y] @ [%H:%M:%S]")))
                lf.write("\n" + int_msg + "Date/Time: %s\n" % (datetime.now().strftime("[%m-%d-%y] @ [%H:%M:%S]")))

                def send_attacker_msg(message):
                    attacker.send(message)
                    attacker.close()
                    ip_list.append(attacker_ip)

                def recv_attacker_msg(ph):
                    try:
                        data = attacker.recv(1024)
                        got_msg = True
                    except:
                        print("Data: Connection returned no data...")
                        print("-"*30+"\n")
                        lf.write("-"*30+"\n")

                        got_msg = False
                    finally:
                        if (got_msg):
                            print("Data: Returned data, placed in log...")
                            print("-"*30+"\n")
                            lf.write("Header: \n\n%s" % format_header(str(data)))
                            lf.write("-"*30+"\n")


                send = threading.Thread (
                    target=send_attacker_msg,
                    args=(msg,)
                )
                get = threading.Thread (
                    target=recv_attacker_msg,
                    args=(None,)
                )

                get.start()
                send.start()

# ______ Main ______
if __name__ == '__main__':
    clear()
    print(banner)

    if (os.path.exists("config")):
        try:
            start_pot(str(read_config()[0]).replace('\n',''), int(read_config()[1]), True)
        except Exception:
            remove_conf(True)
            exit(er + "Broken config! Exiting and removing...")
    else:
        mode = input(sp + "Select Mode (1 = Single-Use, 2 = Config Builder) >> ")

        if (mode == "1"):
            start_pot(get_host_ip(False), get_host_port(False), False)
        elif (mode == "2"):
            build_config()
        else:
            exit(er + "Invalid option. Exitting...")
