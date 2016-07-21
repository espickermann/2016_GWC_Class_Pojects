int PIEZOPIN = 5;
int PINLIGHT = 4;

// One octave of notes between n_A4 and A5
int n_A4 = 440;
int n_As4 = 466; int note_Bn_B4 = n_As4;
int n_B4 = 494;
int n_C5 = 523;
int n_Cs5 = 554; int n_Db5 = n_Cs5;
int n_D5 = 587;
int n_Ds5 = 622; int n_Eb5 = n_Ds5;
int n_E5 = 659;
int n_F5 = 698;
int n_Fs5 = 740; int n_Gb5 = n_Fs5;
int n_G5 = 784;
int n_Gs5 = 830; int n_Ab5 = n_Gs5;

// int note_A5 = note_n_A4 * 2;
// int note_As5 = n_As4 * 2; int note_Bb5 = note_As5;
// int note_B5 = note_n_B4 * 2;

int note_rest = -1;

// note lengths defined here
long whole = 1600; // change tempo by changing duration of one measure
long half = whole / 2;
long quarter = whole / 4;
long eighth = whole / 8;
long sixteenth = whole / 16;

// WRITE YOUR SONG HERE
int song[42][2] = {{n_C5, quarter}, {n_C5, quarter}, {n_G5, quarter}, {n_G5, quarter}, {n_A4, quarter}, {n_A4, quarter}, {n_G5, half},
                           {n_F5, quarter}, {n_F5, quarter}, {n_E5, quarter}, {n_E5, quarter}, {n_D5, quarter}, {n_D5, quarter}, {n_C5, half},
                           {n_G5, quarter}, {n_G5, quarter}, {n_F5, quarter}, {n_F5, quarter}, {n_E5, quarter}, {n_E5, quarter}, {n_D5, half},
                           {n_G5, quarter}, {n_G5, quarter}, {n_F5, quarter}, {n_F5, quarter}, {n_E5, quarter}, {n_E5, quarter}, {n_D5, half},
                           {n_C5, quarter}, {n_C5, quarter}, {n_G5, quarter}, {n_G5, quarter}, {n_A4, quarter}, {n_A4, quarter}, {n_G5, half},
                           {n_F5, quarter}, {n_F5, quarter}, {n_E5, quarter}, {n_E5, quarter}, {n_D5, quarter}, {n_D5, quarter}, {n_C5, half}};
  
// if you want there to be silence between notes,
//   staccato should be true
bool staccato = true;

void setup() {
  pinMode(PIEZOPIN, OUTPUT);
}

void loop() {
  
  //PLAY YOUR SONG HERE
  for(int i = 0; i<43; i++){
    //Serial.println(song[i][i])
    tone(PIEZOPIN, song[i][0]);
    //put high here
    delay(song[i][1]);
    tone(PIEZOPIN, 65535);
    //low here
    delay(10);
  }

}
