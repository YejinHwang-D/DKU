package hwangyejin;
import java.util.Scanner;

public class ArrSort {

	public static void main(String[] args) {	
		for (int count = 0; count < 3; count++) {
			Scanner sc = new Scanner(System.in);
			System.out.printf("n �� �Է�: ");
			int n = sc.nextInt(), temp; //n�� �� �Է� �ޱ�, temp ���� ����
			int[] arr = new int[n]; //�迭 �ʱ�ȭ
			
			System.out.printf("%d ���� ���� �Է�: ", n);
			for(int i = 0 ; i < n ; i++) { //n�� ��ŭ ���� �Է¹ޱ�
				arr[i] = sc.nextInt();
			}
			
			for (int i=0; i<n; i++) { //���� ����
				for (int j = 1; j<n; j++) { //ù��° index���� ��
					if (arr[j-1] > arr [j]) { //ù��° ���� �ι�° ������ Ŭ ��
						temp = arr[j-1]; //ù��°�� �ι�° �ڸ� ��ü
						arr[j-1] = arr[j];
						arr[j] = temp;
					}
				} //
			}
			System.out.printf("���İ�� : ");
			for(int i = 0 ; i < n ; i++) { //���ĵ� �迭 �� ���
				System.out.printf("%d ",arr[i]);
			}
			System.out.println("\n");
		}
	}
}
