#include <VirtualWire.h>

const int transmit_pin = 4;
const int receive_pin = 2;
const int transmit_en_pin = 3;
const int jx = A3 ;
const int jy = A2 ;
const int sw = 2 ;



void setup()
{
  Serial.begin(9600) ;
  // Initialise the IO and ISR
  vw_set_tx_pin(transmit_pin);
  vw_set_rx_pin(receive_pin);
  vw_set_ptt_pin(transmit_en_pin);
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(2000);   // Bits per sec
  pinMode(LED_BUILTIN, OUTPUT) ;
  pinMode(sw, INPUT) ;

}

byte count = 1;

void loop()
{
  int x = map(analogRead(jx), 0, 1023, 0, 100) ;
  int y = map(analogRead(jy), 0, 1023, 0, 100) ;

  if ( x > 55 || x < 45 || y > 55 || y < 45 ) {
    Serial.print(x) ;
    Serial.print(", ") ;
    Serial.print(y) ;
    Serial.print(", ") ;
    Serial.println(digitalRead(sw)) ;
    char msg[3] = {x, y, digitalRead(sw)} ;
    digitalWrite(LED_BUILTIN, HIGH); // Flash a light to show transmitting
    vw_send((uint8_t *)msg, 3);
    vw_wait_tx(); // Wait until the whole message is gone
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(200);
}
