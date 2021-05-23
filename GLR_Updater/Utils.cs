using System;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net;
using System.IO;
using System.IO.Compression;
using System.Diagnostics;

namespace GLR_Updater {
   class Utils {
      public static async Task<string> GetLatest() {
         ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3;

            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls11 | SecurityProtocolType.Tls12;
         using (var httpClient = new HttpClient()) {
            HttpResponseMessage response = await httpClient.GetAsync("https://github.com/ImaniiTy/GreenLuma-Reborn-Manager/releases/latest");
            var header = response.RequestMessage.RequestUri.Segments;
            return header.Last().Substring(1);
         }
      }

      public static Task DownloadAndExtractFile(string URL) {
         using (var client = new WebClient()) {
            client.Proxy = null;
            client.DownloadFileCompleted += new System.ComponentModel.AsyncCompletedEventHandler(CompletedHandler);
            client.DownloadProgressChanged += new DownloadProgressChangedEventHandler(ProgressHandler);
            return client.DownloadFileTaskAsync(new Uri(URL), "Release.zip");
         }
      }

      private static void ProgressHandler(object sender, DownloadProgressChangedEventArgs e) {
         Console.Write(String.Format("{0}%\r", e.ProgressPercentage.ToString()));
      }

      private static void CompletedHandler(object sender, System.ComponentModel.AsyncCompletedEventArgs e) {
         ExtractFile("./Release.zip");
         Process.Start("GreenLuma Reborn Manager.exe","-NoUpdate -PostUpdate");
      }

      public static void ExtractFile(string path) {
         Console.WriteLine("Extracting File...");
         using (ZipArchive archive = ZipFile.OpenRead(path)) {
            foreach (ZipArchiveEntry entry in archive.Entries) {
               var fileName = entry.FullName.Split('/')[1];
               if (fileName != "") {
                  Console.WriteLine(Path.Combine("./", fileName));
                  try {
                     entry.ExtractToFile(Path.Combine("./", fileName), true);
                  } catch (Exception e) {
                     entry.ExtractToFile(Path.Combine("./", "new_" + fileName), true);
                  }
               }
            }
         }

         Console.WriteLine("Deleting Temporary Files...");
         File.Delete(path);
      }

      public static StreamWriter CreateLogger() {
         FileStream logOutput = new FileStream("UpdaterLog.txt", FileMode.Create);
         StreamWriter logWriter = new StreamWriter(logOutput);
         logWriter.AutoFlush = true;

         return logWriter;
      }
   }
}
