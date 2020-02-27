from PCANBasic import *

obj_PCANBasic = PCANBasic()

MSG = obj_PCANBasic.Initialize(PCAN_USBBUS1,PCAN_BAUD_500K)

if MSG != PCAN_ERROR_OK:
    print('CAN FAIL')
else:
    print('CAN SUCESS')


readResult = PCAN_ERROR_OK,
while (readResult[0] & PCAN_ERROR_QRCVEMPTY) != PCAN_ERROR_QRCVEMPTY:
    # Check the receive queue for new messages
    #
    readResult = obj_PCANBasic.Read(PCAN_USBBUS1)
    if readResult[0] != PCAN_ERROR_QRCVEMPTY:
        # Process the received message
        #
        print("A message was received")
        ProcessMessage(result[1],result[2]) # Possible processing function, ProcessMessage(msg,timestamp)
    else:
        # An error occurred, get a text describing the error and show it
        #
        result = obj_PCANBasic.GetErrorText(readResult[0])
        print(result[1])

