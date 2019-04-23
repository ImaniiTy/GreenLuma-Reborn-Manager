using System;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net;
using System.IO;
using System.IO.Compression;

namespace GLR_Updater {
   class Utils {
      public static async Task<string> GetLatest() {
         using (var httpClient = new HttpClient()) {
            HttpResponseMessage response = await httpClient.GetAsync("https://github.com/ImaniiTy/GreenLuma-Reborn-Manager/releases/latest");
            var header = response.RequestMessage.RequestUri.Segments;
            return header.Last().Substring(1);
         }
      }

      public static void downloadFile(string URL) {
         using (var client = new WebClient()) {
            client.Proxy = null;
            Console.WriteLine("Downloading Latest Version...");
            client.DownloadFile(URL, "Release.zip");
            Console.WriteLine("Download Completed!");
         }
      }

      public static void extractFile() {
         using (ZipArchive archive = ZipFile.OpenRead("./Release.zip")) {
            foreach (ZipArchiveEntry entry in archive.Entries) {
               var fileName = entry.FullName.Split('/')[1];
               if (fileName != "") {
                  Console.WriteLine(Path.Combine("./", fileName));
                  entry.ExtractToFile(Path.Combine("./", fileName),true);
               }
            }
         }
      }
   }
}
