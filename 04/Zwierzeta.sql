CREATE TABLE [dbo].[Zwierzeta](
	[zwierze] [varchar](50) NULL,
	[maksymalna_ilosc_lat] [int] NULL,
	[maksymalna_ilosc_kg] [int] NULL
) ON [PRIMARY]
GO

INSERT INTO Zwierzeta (zwierze, maksymalna_ilosc_lat, maksymalna_ilosc_kg) VALUES
('kakadu', 60, 1),
('słoń', 70, 5000),
('gepard', 12, 60),
('mysz polna', 5, 0.03),
('nosorożec', 50, 2000),
('wilk', 16, 90),
('niedźwiedź', 40, 500),
('hipopotam', 45, 3500);
