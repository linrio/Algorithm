package ticketingsystem;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int routenum = 5;     //车次总数
		int coachnum = 8;     //列车的车厢数
		int seatnum = 100;    //每节的座位数
		int stationnum = 10;  //经停站点数
		TicketingDS tds = new TicketingDS(routenum, coachnum, seatnum, stationnum);
		for (int i = 0; i < 1; i++){
			Thread thread = new Thread(){
				public void run(){
					String passenger = "linlingfeng";
					int route = 3;
					int departure = 4;
					int arrival = 6;
					Ticket ticket = tds.buyTicket(passenger, route, departure, arrival);
					System.out.println("票号为 " + ticket.tid + " 的 "+ ticket.passenger + 
					" 乘客购买了车次为 "+ticket.route +" 车厢为 " +ticket.coach +" 座位号为 " +ticket.seat +
					" 的从第 " + ticket.departure +" 站到第 " +ticket.arrival + " 站的车票一张.");
					
					int num;
					int departure2 = 7;
					int arrival2 = 8;
					num = tds.inquiry(route, departure2, arrival2);
					System.out.println("车次为" + ticket.route + "的从第" + ticket.departure + 
							"站到第" + ticket.arrival + "站的余票为" + num +"张.");
				}
			};
			thread.start();
		}
	}		
}
