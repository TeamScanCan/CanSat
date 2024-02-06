#include "LoRa.h"

/* 
Modified ping example, based on sx1278-LoRa-RaspberryPi library.
*/

void * rx_f(void *p){
    rxData *rx = (rxData *)p;
    LoRa_ctl *modem = (LoRa_ctl *)(rx->userPtr);
    printf("string: %s\n", rx->buf);//Data we've received
    LoRa_stop_receive(modem);
    free(p);
    return NULL;
}

void tx_f(txData *tx){
    LoRa_ctl *modem = (LoRa_ctl *)(tx->userPtr);
    printf("string: %s\n", tx->buf);//Data we've sent
    LoRa_receive(modem);
}

void setTxData(txData *tx, char *data)
{
    int txLen = strlen(data) + 1;
    tx->size = txLen;
    memcpy(tx->buf, data, txLen);
}
int main(){
    LoRa_ctl modem;
    char txbuf[255];

    //See for typedefs, enumerations and there values in LoRa.h header file
    modem.spiCS = 0;//Raspberry SPI CE pin number
    modem.rx.callback = rx_f;
    modem.tx.callback = tx_f;
    modem.tx.data.buf = txbuf;
    modem.eth.preambleLen=6;
    modem.eth.bw = BW62_5;//Bandwidth 62.5KHz
    modem.eth.sf = SF12;//Spreading Factor 12
    modem.eth.ecr = CR8;//Error coding rate CR4/8
    modem.eth.freq = 434800000;// 434.8MHz
    modem.eth.resetGpioN = 4;//GPIO4 on lora RESET pi
    modem.eth.dio0GpioN = 17;//GPIO17 on lora DIO0 pin to control Rxdone and Txdone interrupts
    modem.eth.outPower = OP20;//Output power
    modem.eth.powerOutPin = PA_BOOST;//Power Amplifire pin
    modem.eth.AGC = 1;//Auto Gain Control
    modem.eth.OCP = 240;// 45 to 240 mA. 0 to turn off protection
    modem.eth.implicitHeader = 0;//Explicit header mode
    modem.eth.syncWord = 0x12;
    
    LoRa_begin(&modem);
    LoRa_receive(&modem);

    char str_data[255];

    while(1 == 1)
    {
        for(int i = 0; i < 40; i++)
        {
            sprintf(str_data, "%d", i);
            setTxData(&modem.tx.data, str_data);
            LoRa_send(&modem);
            sleep(((int)modem.tx.data.Tpkt/1000)+1);
        }
    }
    printf("end\n");
    LoRa_end(&modem);
}
