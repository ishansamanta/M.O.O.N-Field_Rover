#include <Servo.h>

// ==========================================
// PIN DEFINITIONS 
// ==========================================

// Ultrasonic Sensor
#define TRIG_PIN A0
#define ECHO_PIN A1

// Camera & Sensor Pan Servo (180-degree)
#define PAN_SERVO_PIN 4

// Left Motor (BTS7960)
#define L_RPWM 3   
#define L_LPWM 5   
#define L_REN 7    
#define L_LEN 8    

// Right Motor (BTS7960)
#define R_RPWM 6   
#define R_LPWM 11  
#define R_REN 10   
#define R_LEN 12   

// Linear Actuators (MG996R 360-degree Continuous Rotation)
#define DRILL_SERVO_1 A2 
#define DRILL_SERVO_2 A3 
#define NPK_SERVO_1 A4   
#define NPK_SERVO_2 A5   

// Drill DC Motor Relay
#define DRILL_RELAY 2

// ==========================================
// OBJECTS & VARIABLES
// ==========================================
Servo panServo;
Servo drillServo1;
Servo drillServo2;
Servo npkServo1;
Servo npkServo2;

bool menuPrinted = false;

void setup() {
  Serial.begin(9600); 

  // --- Hardware Setup ---
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(L_RPWM, OUTPUT);
  pinMode(L_LPWM, OUTPUT);
  pinMode(L_REN, OUTPUT);
  pinMode(L_LEN, OUTPUT);
  
  pinMode(R_RPWM, OUTPUT);
  pinMode(R_LPWM, OUTPUT);
  pinMode(R_REN, OUTPUT);
  pinMode(R_LEN, OUTPUT);

  digitalWrite(L_REN, HIGH);
  digitalWrite(L_LEN, HIGH);
  digitalWrite(R_REN, HIGH);
  digitalWrite(R_LEN, HIGH);

  pinMode(DRILL_RELAY, OUTPUT);
  digitalWrite(DRILL_RELAY, LOW); 

  panServo.attach(PAN_SERVO_PIN);
  drillServo1.attach(DRILL_SERVO_1);
  drillServo2.attach(DRILL_SERVO_2);
  npkServo1.attach(NPK_SERVO_1);
  npkServo2.attach(NPK_SERVO_2);

  // --- Initial States ---
  drillServo1.write(90); 
  drillServo2.write(90);
  npkServo1.write(90);
  npkServo2.write(90);
  panServo.write(90); 

  delay(1000); // Give hardware a second to stabilize
}

void loop() {
  if (!menuPrinted) {
    printMenu();
    menuPrinted = true;
  }

  if (Serial.available() > 0) {
    char cmd = Serial.read();
    
    // Ignore invisible line ending characters
    if (cmd == '\n' || cmd == '\r' || cmd == ' ') return;
    
    // Convert lowercase to uppercase to make it easy
    cmd = toupper(cmd);
    
    executeMenuCommand(cmd);
    
    // Wait a brief moment, then reprint the menu prompt
    delay(200);
    Serial.println("\n--- Command Executed. Awaiting next input... (Send 'M' to see menu again) ---");
  }
}

// ==========================================
// MENU UI & EXECUTION
// ==========================================

void printMenu() {
  Serial.println("\n=================================");
  Serial.println("  🚜 AGRITECH ROVER - TEST MENU  ");
  Serial.println("=================================");
  Serial.println("[ ROVER MOVEMENT ]");
  Serial.println("  W - Drive Forward");
  Serial.println("  S - Drive Reverse");
  Serial.println("  X - STOP Rover");
  Serial.println("  A - Spin Left");
  Serial.println("  D - Spin Right");
  Serial.println("\n[ DRILL ACTUATOR ]");
  Serial.println("  1 - Move DOWN into soil");
  Serial.println("  2 - Move UP out of soil");
  Serial.println("  3 - STOP Drill Actuator");
  Serial.println("\n[ NPK ACTUATOR ]");
  Serial.println("  4 - Move DOWN into soil");
  Serial.println("  5 - Move UP out of soil");
  Serial.println("  6 - STOP NPK Actuator");
  Serial.println("\n[ DRILL DC MOTOR ]");
  Serial.println("  O - Turn Drill ON");
  Serial.println("  F - Turn Drill OFF");
  Serial.println("\n[ CAMERA & SENSOR ]");
  Serial.println("  C - Center Camera (90 deg)");
  Serial.println("  L - Pan Left (0 deg)");
  Serial.println("  R - Pan Right (180 deg)");
  Serial.println("  U - Read Ultrasonic Distance");
  Serial.println("=================================");
  Serial.println("Type a SINGLE letter or number and hit Enter:");
}

void executeMenuCommand(char cmd) {
  switch (cmd) {
    // --- MOVEMENT ---
    case 'W': driveRover(200, 200); Serial.println(">> Driving FORWARD"); break;
    case 'S': driveRover(-200, -200); Serial.println(">> Driving REVERSE"); break;
    case 'X': driveRover(0, 0); Serial.println(">> Rover STOPPED"); break;
    case 'A': driveRover(-150, 150); Serial.println(">> Spinning LEFT"); break;
    case 'D': driveRover(150, -150); Serial.println(">> Spinning RIGHT"); break;

    // --- DRILL ACTUATOR ---
    case '1': moveDrillActuator(true); Serial.println(">> Drill Actuator: DOWN"); break;
    case '2': moveDrillActuator(false); Serial.println(">> Drill Actuator: UP"); break;
    case '3': stopDrillActuator(); Serial.println(">> Drill Actuator: STOPPED"); break;

    // --- NPK ACTUATOR ---
    case '4': moveNPKActuator(true); Serial.println(">> NPK Actuator: DOWN"); break;
    case '5': moveNPKActuator(false); Serial.println(">> NPK Actuator: UP"); break;
    case '6': stopNPKActuator(); Serial.println(">> NPK Actuator: STOPPED"); break;

    // --- DRILL MOTOR ---
    case 'O': digitalWrite(DRILL_RELAY, HIGH); Serial.println(">> Drill Motor: ON"); break;
    case 'F': digitalWrite(DRILL_RELAY, LOW); Serial.println(">> Drill Motor: OFF"); break;

    // --- CAMERA PAN ---
    case 'C': panServo.write(90); Serial.println(">> Camera: CENTER"); break;
    case 'L': panServo.write(0); Serial.println(">> Camera: LEFT"); break;
    case 'R': panServo.write(180); Serial.println(">> Camera: RIGHT"); break;

    // --- SENSORS & SYSTEM ---
    case 'U': 
      Serial.print(">> Ultrasonic Distance: "); 
      Serial.print(readUltrasonic()); 
      Serial.println(" cm"); 
      break;
    case 'M': 
      printMenu(); 
      break;
      
    default:
      Serial.println(">> INVALID COMMAND. Send 'M' to see the menu.");
      break;
  }
}

// ==========================================
// HARDWARE CONTROL FUNCTIONS
// ==========================================

void driveRover(int left, int right) {
  left = constrain(left, -255, 255);
  right = constrain(right, -255, 255);

  if (left >= 0) {
    analogWrite(L_RPWM, left);
    analogWrite(L_LPWM, 0);
  } else {
    analogWrite(L_RPWM, 0);
    analogWrite(L_LPWM, -left);
  }

  if (right >= 0) {
    analogWrite(R_RPWM, right);
    analogWrite(R_LPWM, 0);
  } else {
    analogWrite(R_RPWM, 0);
    analogWrite(R_LPWM, -right);
  }
}

void moveDrillActuator(bool down) {
  if (down) {
    drillServo1.write(180); 
    drillServo2.write(0);   
  } else {
    drillServo1.write(0);   
    drillServo2.write(180); 
  }
}

void stopDrillActuator() {
  drillServo1.write(90); 
  drillServo2.write(90);
}

void moveNPKActuator(bool down) {
  if (down) {
    npkServo1.write(180);
    npkServo2.write(0);
  } else {
    npkServo1.write(0);
    npkServo2.write(180);
  }
}

void stopNPKActuator() {
  npkServo1.write(90);
  npkServo2.write(90);
}

long readUltrasonic() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  long duration = pulseIn(ECHO_PIN, HIGH, 30000); 
  if (duration == 0) return -1; 
  return duration * 0.0343 / 2; 
}