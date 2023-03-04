GitHubCalendar(".calendar", "LawnShogan");
          
// or enable responsive functionality:
GitHubCalendar(".calendar", "LawnShogan", { responsive: true });

// Use a proxy
GitHubCalendar(".calendar", "LawnShogan", {
   proxy (LawnShogan) {
     return fetch(`https://github.com/lawnshogan`)
   }
}).then(r => r.text())