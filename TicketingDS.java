package ticketingsystem;

public class TicketingDS implements TicketingSystem {

	public TicketingDS(int routenum, int coachnum, int seatnum, int stationnum){}
	Ticket ticket = new Ticket();
	
	
	
	@Override
	public Ticket buyTicket(String passenger, int route, int departure, int arrival) {
		// TODO Auto-generated method stub
		int k = route;
		
		//检索每一张座位的区间。看看我的座位的区间在不在别人的区间内。
		for (int i = 1; i <= 8*100; i++){
			if (ticket.passenger ==null){
				if ((departure >= ticket.arrival) | (arrival <= ticket.departure)){
					ticket.tid = k*1000 + i/100+100 + i%100;
					ticket.passenger = passenger;
					ticket.route = route;
					ticket.coach = i/100+1;
					ticket.seat = i%100;
					ticket.departure = departure;
					ticket.arrival = arrival;
					System.out.println(ticket);
					return ticket;
				}
			}
		}
		return null;
	}
	
	
	@Override
	public int inquiry(int route, int departure, int arrival) {
		// TODO Auto-generated method stub
		int k = route;
		int count = 0;
		for (int i = 1; i <= 8*100; i++){
			ticket.seat = i%100;
			if (ticket.passenger == null){
				if ((departure >= ticket.arrival) | (arrival <= ticket.departure)){
					count ++;
					System.out.println(count);
					}
			}
		}
		
		return count;
	}
	@Override
	public boolean refundTicket(Ticket ticket) {
		// TODO Auto-generated method stub
		return false;
	}

}
