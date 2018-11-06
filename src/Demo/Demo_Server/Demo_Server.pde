import processing.net.*;

// TCP Connection Parameters
int port = 10002;
Server demoServer;

// Background
PImage img;


// Tiles Parameter
Tile[][][] tiles;
int group = 7;
int cols = 27;
int rows = 27;
int pixel_s = 4;


void setup() {
  // Background
  img = loadImage("Chub.jpg");
  image(img, 0, 0);


  // TCP Connection Setup
  demoServer = new Server(this, port);

  // Tiles Demo Setup
  size(897, 1191);
  // background(255);
  tiles = new Tile[group][cols][rows];
  int[] col_p = {3, 8, 15, 28, 33, 38, 46, 52, 57, 64, 77, 82, 87, 95, 101, 106, 113, 124, 129, 134, 142, 148, 154, 174, 179, 184, 193};

  for (int i = 0; i<group; i++) {
    for (int j = 0; j<cols; j++) {
      for (int k = 0; k<rows; k++) {
        tiles[i][j][k]=new Tile(col_p[j], i*135+k*(pixel_s+1), pixel_s, pixel_s);
        // tiles[i][j][k].display();
      }
    }
  }
}

void draw() {
    translate(350,20);
  // Reading msg via TCP
  // Get the next available client
  Client demoClient = demoServer.available();

  if (demoClient !=null) {
    String clientMsg = demoClient.readString();
    if (clientMsg != null) {
      println(demoClient.ip() + " : " + clientMsg);
      switch(clientMsg) {

      case "q":
        demoServer.stop();

      case "test":
        demoServer.write("Demo Server Activated");

      default:
        // Interprete the Message from clients
        String[] clientCommand = split(clientMsg, '&');
        for (int x=0; x<clientCommand.length; x++) {
          String[] commandPara = split(clientCommand[x], '=');

          //command exception
          if (commandPara.length < 2) {
            demoServer.write("command_error");  
            break;
          }

          String[] tileList = split(commandPara[0], ',');

          int tile_new_color = int(commandPara[1]);       
          if (tile_new_color > 255) {
            tile_new_color = 255;
          } else if (tile_new_color <0) {
            tile_new_color = 0;
          }
          for (int y=0; y<tileList.length; y++) {
            int[] tileNum = int(split(tileList[y], '-'));
            tiles[tileNum[0]][tileNum[1]][tileNum[2]].tile_color = tile_new_color;
          }
        }
        demoServer.write("OK");
      }
    }
  }

  // Display Demo Tiles

  for (int i = 0; i<group; i++) {
    for (int j = 0; j<cols; j++) {
      for (int k = 0; k<rows; k++) {
        tiles[i][j][k].display();
      }
    }
  }
}

class Tile {
  int X;
  int Y;
  int size_X;
  int size_Y;
  int tile_color;

  Tile(int temp_X, int temp_Y, int temp_sX, int temp_sY) {
    X = temp_X;
    Y = temp_Y;
    size_X = temp_sX;
    size_Y = temp_sY;
    tile_color = 255;
  }

  void display() {
    pushMatrix();
    translate(X, Y);
    stroke(0);
    fill(tile_color);
    rect(0, 0, size_X, size_Y);
    popMatrix();
  }
}
