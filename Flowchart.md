:::mermaid

    flowchart TD
    A(Start) --> B[Menampilkan daftar menu peralatan dan cara pembayaran]
    B --> C[/Input menu/]
    C --> D[/Input jumlah pemesanan/]
    D --> E[/Input cara pembayaran/]
    E --> F{Jika Jumlah Pembelian Diatas 300rb maka mendapatkan diskon 10%}
    F -- Yes --> G[Diskon=Jumlah Pembelian X 10%, Total=Jumlah Pembelian - Diskon]
    F -- No --> H
    G --> H[Menampilkan Detail Pembayaran]
    H --> I(End)
:::
