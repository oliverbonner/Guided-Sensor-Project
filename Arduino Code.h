int PacketHeader = 65535;

enum _PacketID{
  TEMP,
  PULSE_OXI
};

_PacketID TemperaturePacket = TEMP;
_PacketID PulseOximeterPacket = PULSE_OXI;

void WritePacket(_PacketID PacketID);
